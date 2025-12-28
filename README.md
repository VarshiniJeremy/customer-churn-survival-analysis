Customer Churn Survival Analysis

This project analyzes customer churn using survival analysis techniques.  
Instead of predicting only whether a customer will churn, this project focuses on when churn is likely to happen and which factors affect customer retention over time.


1. Project Motivation

Traditional churn models treat churn as a binary classification problem.  
However, in real business scenarios, time matters.

This project aims to:
- Model churn as a time-to-event problem
- Estimate customer survival probability over time
- Identify risk factors that increase or reduce churn
- Segment customers based on churn risk

2. Dataset Description

- The dataset is **synthetically generated** to resemble a telecom customer dataset
- Number of customers: ~7000
- Time variable: `tenure` (in months)
- Event variable: `Churn` (Yes / No)

The dataset generation logic is available in: data_generation.py

3. Project Structure
   customer-churn-survival-analysis/
│
├── churn_survival_analysis.ipynb # Main analysis notebook
├── data_generation.py # Synthetic data generation
├── churn_data.csv # Generated dataset
├── cox_hazard_ratios.csv # Cox model results
└── README.md

4. 4. Methodology

4.1 Survival Analysis
- Customer churn is treated as an event
- Tenure represents the time until churn
- Kaplan–Meier estimator is used to:
  - Plot overall survival probability
  - Compare survival across different customer segments

4.2 Cox Proportional Hazards Model
- Used to quantify the effect of features on churn risk
- Outputs hazard ratios:
  - HR > 1 → higher churn risk
  - HR < 1 → lower churn risk
- Top features are visualized with **95% confidence intervals**

4.3 Risk Scoring and Segmentation
- Individual customer risk scores are computed
- Customers are grouped into:
  - Low risk
  - Medium risk
  - High risk
  - Very high risk
- Risk distributions and counts are visualized


5. Visual Analysis Included

- Overall customer survival curve
- Survival curves based on:
  - Contract type
  - Payment method
  - Tech support availability
  - Internet service type
- Top 15 features by hazard ratio
- Distribution of customer risk scores
- Customer count by risk category


6. Key Observations

- Customers with month-to-month contracts churn significantly faster
- Two-year contracts show the highest retention
- Customers with tech support have better survival probability
- Higher tenure strongly reduces churn risk
- Certain payment methods are associated with slightly higher churn


7. How to run the project

Step 1: Clone the repository
git clone https://github.com/VarshiniJeremy/customer-churn-survival-analysis.git
cd customer-churn-survival-analysis

Step 2: Install required libraries
pip install numpy pandas matplotlib seaborn lifelines

Step 3: Generate dataset
python data_generation.py

Step 4: Open churn_survival_analysis.ipynb in:

VS Code (Python extension)

Run all cells sequentially.
