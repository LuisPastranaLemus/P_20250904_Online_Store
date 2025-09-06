import numpy as np
import pandas as pd

# Import function directly (more controlled than import *)
from src import *

def cast_datatypes(df, cast_type, numeric_type=None, date_format=None, c_time_zone=None, c_include=None, c_exclude=None):
    
    if c_exclude is None:
        c_exclude = []

    if c_include is None:
        available_columns = [col for col in df.columns if col not in c_exclude]
    else:
        available_columns = [col for col in c_include if col not in c_exclude]

    if cast_type == 'string':
        for column in available_columns:
            df[column] = df[column].astype("string")
    
    elif cast_type == 'numeric':
        df = convert_object_to_numeric(df, type=numeric_type, include=c_include, exclude=c_exclude)
    
    elif cast_type == 'category':
        for column in available_columns:
            df[column] = df[column].astype("category")
    
    elif cast_type == 'boolean':
        for column in available_columns:
            if df[column].dropna().isin([0, 1]).all():
                df[column] = df[column].astype("boolean")
            else:
                df[column] = df[column].astype("Int64").astype("boolean")
    
    elif cast_type == 'datetime':
        tz = c_time_zone if c_time_zone is not None else ""
        df = normalize_datetime(df, include=c_include, exclude=c_exclude, frmt=date_format, time_zone=tz)

    else:
        raise ValueError(f"Unsupported cast_type: {cast_type}")
    
    return df
    
# ICE priorization method
def ice_prioritization(df, method="ease"):
    """
    Calculate ICE score for hypothesis prioritization.

    Methods:
    - "effort": ICE = (Impact * Confidence) / Effort
      Requires columns: 'impact', 'confidence', 'effort'
    - "ease":    ICE = Impact * Confidence * Ease
      Requires columns: 'impact', 'confidence', 'ease'
    - "rice":    RICE = (reach * impact * confidence) / effort
      Requires: 'reach', 'impact', 'confidence', 'effort'

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing required columns depending on method.
    method : str, default="ease"
        Method to calculate ICE score. Options: ["effort", "ease"]

    Returns
    -------
    DataFrame with a new column:
      - 'ice_score'  when method in {"effort","ease"}
      - 'rice_score' when method == "rice"
    """

    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    # Define columns according to method chosen
    if method == "effort":
        required_cols = {"impact", "confidence", "effort"}
        score_col = "ice_score"
    elif method == "ease":
        required_cols = {"impact", "confidence", "ease"}
        score_col = "ice_score"
    elif method == "rice":
        required_cols = {"reach", "impact", "confidence", "effort"}
        score_col = "rice_score"
    else:
        raise ValueError("Invalid method. Use 'effort', 'ease', or 'rice'.")

    # Required columns validation
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns for {method} method: {missing_cols}")

    # Null values validation
    if df[list(required_cols)].isnull().any().any():
        raise ValueError(f"Columns {required_cols} must not contain null values.")

    # Guard rails for division
    if method in {"effort", "rice"} and (df["effort"] == 0).any():
        raise ZeroDivisionError("Column 'effort' contains zero(s); cannot divide by zero.")
    
    # Optional: ensure numeric types (will raise if non-numeric present)
    numeric_check = df[list(required_cols)].apply(pd.to_numeric, errors="raise")

    # Copy DataFrame
    df = df.copy()

    # Calcular ICE/RICE según método
    if method == "effort":
        df[score_col] = (df["impact"] * df["confidence"]) / df["effort"]
    elif method == "ease":
        df[score_col] = df["impact"] * df["confidence"] * df["ease"]
    else:  # "rice"
        df[score_col] = (df["reach"] * df["impact"] * df["confidence"]) / df["effort"]

    return df

# WSJK priorization method    
def wsjf_prioritization(df):
    """
    Calculate WSJF (Weighted Shortest Job First) score for prioritization.

    WSJF = Cost of Delay / Job Duration
    Cost of Delay = User Business Value + Time Criticality + Risk Reduction/Opportunity Enablement

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing columns:
        - 'user_business_value'
        - 'time_criticality'
        - 'risk_reduction'
        - 'job_duration'

    Returns
    -------
    pd.DataFrame
        Original DataFrame with two new columns:
        - 'cost_of_delay'
        - 'wsjf_score'
    """

    # 1. Input validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    # 2. Define columns
    required_cols = {"user_business_value", "time_criticality", "risk_reduction", "job_duration"}
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # 3. Null values validation
    if df[list(required_cols)].isnull().any().any():
        raise ValueError(f"Columns {required_cols} must not contain null values.")

    # 4. job_duration validation
    if (df["job_duration"] == 0).any():
        raise ZeroDivisionError("Column 'job_duration' contains zero(s), cannot divide by zero.")

    # 5. Copy DataFrame
    df = df.copy()

    # 6. Cost of Delay calculation
    df["cost_of_delay"] = (df["user_business_value"] + df["time_criticality"] + df["risk_reduction"])

    # 7. WSJF calculation
    df["wsjf_score"] = df["cost_of_delay"] / df["job_duration"]

    return df