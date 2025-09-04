# 🧭 Project Analysis
Brief Decription

---

## 🔍 Project Overview (P-20250904_Online_Store)

The goal is to explore how data-driven decision making can increase the revenue of a large online store by:

- Prioritizing business hypotheses using the ICE and RICE frameworks.
- Running and analyzing an A/B test to evaluate the impact of these hypotheses on key metrics such as revenue, average order value, and conversion rate.

The project is divided into two parts:

- Hypothesis Prioritization – Ranking business ideas based on potential impact, reach, confidence, and required effort.
- A/B Test Analysis – Evaluating statistical significance, identifying anomalies, and drawing actionable business conclusions.

Project Info explanation

__Note__: Make a decision based on the test results. Possible decisions are:   
1. Stop the test and consider one of the groups the leader.   
2. Stop the test and conclude that there is no difference between the groups. 3. Continue the test.   

---

## 🧮 Data Dictionary

This project has 3 different datasets.

- `hypotheses_us.csv` (Hypotheses metrics)
    `Hypotheses`: Brief descriptions of the hypotheses.
    `Reach`: User reach, on a scale of one to ten.
    `Impact`: Impact on users, on a scale of one to ten.
    `Confidence`: Confidence in the hypothesis, on a scale of one to ten.
    `Effort`: The resources required to test a hypothesis, on a scale of one to ten. The higher the Effort value, the more resources the test requires.

- `orders_us.csv` (Orders data)
    `transactionId`: Order ID.
    `visitorId`: ID of the user who placed the order.
    `date`: Date of the order.
    `revenue`: Revenue from the order.
    `group`: The A/B test group to which the user belongs.

- `visits_us.csv` (Visits data)
    `date`: The date.
    `group`: A/B test group.
    `visits`: The number of visits on the specified date in the specified A/B test group.

---

## 📚 Guided Foundations (Historical Context)

The notebook `00-guided-analysis_foundations.ipynb` reflects an early stage of my data analysis learning journey, guided by TripleTen. It includes data cleaning, basic EDA, and early feature exploration, serving as a foundational block before implementing the improved structure and methodology found in the main analysis.

---

## 📂 Project Structure

```bash
├── data/
│   ├── raw/              # Original dataset(s) in CSV format
│   ├── interim/          # Intermediate cleaned versions
│   └── processed/        # Final, ready-to-analyze dataset
│
├── notebooks/
│   ├── 00-guided-analysis_foundations.ipynb     ← Initial guided project (TripleTen)
│   ├── 01_cleaning.ipynb                        ← Custom cleaning 
│   ├── 02_feature_engineering.ipynb             ← Custom feature engineering
│   ├── 03_eda_and_insights.ipynb                ← Exploratory Data Analysis & visual storytelling
│   └── 04-sda_hypotheses.ipynb                  ← Business insights and hypothesis testing
│
├── src/
│   ├── init.py              # Initialization for reusable functions
│   ├── data_cleaning.py     # Data cleaning and preprocessing functions
│   ├── data_loader.py       # Loader for raw datasets
│   ├── eda.py               # Exploratory data analysis functions
│   ├── features.py          # Creation and transformation functions for new variables to support modeling and EDA
│   └── utils.py             # General utility functions for reusable helpers
│
├── outputs/
│   └── figures/          # Generated plots and visuals
│
├── requirements/
│   └── requirements.txt      # Required Python packages
│
├── .gitignore            # Files and folders to be ignored by Git
└── README.md             # This file
```
---

🛠️ Tools & Libraries

- Python 3.11
- os, pathlib, sys, pandas, NumPy, Matplotlib, seaborn, IPython.display, scipy.stats
- Jupyter Notebook
- Git & GitHub for version control
-

---

## 📌 Notes

This project is part of a personal learning portfolio focused on developing strong skills in data analysis, statistical thinking, and communication of insights. Constructive feedback is welcome.

---

## 👤 Author   
##### Luis Sergio Pastrana Lemus   
##### Engineer pivoting into Data Science | Passionate about insights, structure, and solving real-world problems with data.   
##### [GitHub Profile](https://github.com/LuisPastranaLemus)   
##### 📍 Querétaro, México     
##### 📧 Contact: luis.pastrana.lemus@engineer.com   
---

