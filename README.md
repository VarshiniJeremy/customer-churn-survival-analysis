This project applies survival analysis to model time-to-churn for customers instead of treating churn as a simple binary classification problem.
By using Kaplan–Meier estimation and a Cox Proportional Hazards model, the analysis captures when customers are likely to churn and which factors accelerate or delay churn.

The goal is to provide actionable insights for customer retention strategies using statistically sound methods.

1. **Why Survival Analysis for Churn?**

Traditional churn models answer “Will the customer churn?”
Survival analysis answers “When is the customer likely to churn?”

This distinction is critical for:

A. Prioritizing at-risk customers earlier

B. Designing time-sensitive retention campaigns

C. Quantifying the impact of customer attributes on churn risk over time

2. **Dataset Description**

A. File: *churn_data.csv*

B. Each row represents a customer with:

   i) *Duration:* Time observed until churn or censoring

   ii) *Event indicator:*

      1 → Customer churned

      0 → Customer still active (right-censored)

C. *Customer attributes (examples):*

   i) Demographics

   ii) Subscription or usage-related features

   iii) Service or contract characteristics

      Customers who have not churned by the end of observation are right-censored, which is handled natively by survival models.

3. **Technologies Used**

A. Python

B. pandas – data manipulation

C. lifelines – survival analysis modeling

D. matplotlib – visualization

4. **Methodology**
1️⃣ Data Preparation

Cleaned and structured the dataset for time-to-event modeling

Defined:

duration → time until churn or censoring

event → churn indicator

Ensured compatibility with survival modeling assumptions

2️⃣ Kaplan–Meier Survival Estimation

Estimated overall customer survival probability over time

Plotted survival curves to visualize retention patterns

Compared survival curves across customer segments

📈 *Insight:* Survival curves reveal how long different customer groups typically remain active.

3️⃣ Cox Proportional Hazards Model

Fit a Cox model to quantify the effect of customer features on churn risk

Estimated hazard ratios:

HR > 1 → Higher churn risk

HR < 1 → Lower churn risk

Interpreted coefficients in business terms

📊 *Outcome:* Identified key drivers that significantly increase or decrease churn risk.

4️⃣ Model Assumption Checks

Verified the Proportional Hazards assumption

Ensured model validity and interpretability

Flagged variables that may violate assumptions for future refinement

5. **Key Outcomes & Insights**

Clear visualization of customer retention behavior over time

Identification of high-risk customer segments

Quantitative measurement of churn drivers via hazard ratios

A statistically robust alternative to standard churn classification models

6. **Deliverables**

Jupyter Notebook with:

Data preprocessing
Kaplan–Meier survival curves
Cox model fitting and diagnostics

Visualizations comparing survival across segments

Interpretable results suitable for business decision-making
