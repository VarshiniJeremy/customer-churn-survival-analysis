import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of customers
n_customers = 7000

# Generate customer IDs
customer_ids = [f'CUST{str(i).zfill(5)}' for i in range(1, n_customers + 1)]

# Generate features
data = {
    'customerID': customer_ids,
    'gender': np.random.choice(['Male', 'Female'], n_customers),
    'SeniorCitizen': np.random.choice([0, 1], n_customers, p=[0.84, 0.16]),
    'Partner': np.random.choice(['Yes', 'No'], n_customers, p=[0.52, 0.48]),
    'Dependents': np.random.choice(['Yes', 'No'], n_customers, p=[0.30, 0.70]),
    'tenure': np.random.exponential(scale=20, size=n_customers).astype(int).clip(1, 72),
    'PhoneService': np.random.choice(['Yes', 'No'], n_customers, p=[0.90, 0.10]),
    'MultipleLines': np.random.choice(['Yes', 'No', 'No phone service'], n_customers, p=[0.45, 0.45, 0.10]),
    'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], n_customers, p=[0.35, 0.50, 0.15]),
    'OnlineSecurity': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.30, 0.55, 0.15]),
    'OnlineBackup': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.35, 0.50, 0.15]),
    'DeviceProtection': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.35, 0.50, 0.15]),
    'TechSupport': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.30, 0.55, 0.15]),
    'StreamingTV': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.40, 0.45, 0.15]),
    'StreamingMovies': np.random.choice(['Yes', 'No', 'No internet service'], n_customers, p=[0.40, 0.45, 0.15]),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_customers, p=[0.55, 0.21, 0.24]),
    'PaperlessBilling': np.random.choice(['Yes', 'No'], n_customers, p=[0.59, 0.41]),
    'PaymentMethod': np.random.choice([
        'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
    ], n_customers, p=[0.33, 0.23, 0.22, 0.22]),
    'MonthlyCharges': np.random.normal(65, 25, n_customers).clip(18, 120),
}

df = pd.DataFrame(data)

# Calculate TotalCharges based on tenure and monthly charges
df['TotalCharges'] = (df['tenure'] * df['MonthlyCharges']).round(2)

# Generate churn with realistic probabilities based on features
churn_probability = 0.27  # Base probability

# Factors that increase churn risk
churn_scores = np.random.random(n_customers)

# Adjust based on contract type
churn_scores = np.where(df['Contract'] == 'Month-to-month', churn_scores * 1.8, churn_scores)
churn_scores = np.where(df['Contract'] == 'Two year', churn_scores * 0.3, churn_scores)

# Adjust based on tenure (longer tenure = less churn)
churn_scores = churn_scores * np.exp(-df['tenure'] / 30)

# Adjust based on tech support
churn_scores = np.where(df['TechSupport'] == 'No', churn_scores * 1.3, churn_scores)

# Adjust based on monthly charges (higher charges = more churn)
churn_scores = churn_scores * (1 + (df['MonthlyCharges'] - df['MonthlyCharges'].mean()) / 100)

# Convert to binary churn decision
df['Churn'] = np.where(churn_scores > np.percentile(churn_scores, 73), 'Yes', 'No')

# Save to CSV
df.to_csv('churn_data.csv', index=False)

print("✅ Sample churn data generated successfully!")
print(f"📊 Dataset shape: {df.shape}")
print(f"📈 Churn rate: {(df['Churn'] == 'Yes').mean():.2%}")
print(f"💾 Saved to: churn_data.csv")
print("\nFirst few rows:")
print(df.head())