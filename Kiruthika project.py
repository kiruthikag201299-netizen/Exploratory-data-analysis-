#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-29T12:24:38.755Z
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=== Customer Churn Analysis Project ===\n")


print("\n" + "="*50)
print("TASK 2: Initial Data Inspection")
print("="*50)

# Basic dataset info
print("\n1. Dataset Overview:")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Data types
print("\n2. Data Types:")
print(df.dtypes)

# Check for missing values
print("\n3. Missing Values:")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0] if missing_data.sum() > 0 else "No missing values found!")

# Descriptive statistics for numerical features
print("\n4. Descriptive Statistics for Numerical Features:")
numerical_cols = ['Tenure', 'MonthlyCharges', 'TotalCharges', 'Age', 'NumServices', 'SupportCalls']
desc_stats = df[numerical_cols].describe()
print(desc_stats)

# Additional statistics
print("\n5. Additional Statistics:")
for col in numerical_cols:
    print(f"{col}:")
    print(f"  Mean: {df[col].mean():.2f}")
    print(f"  Median: {df[col].median():.2f}")
    print(f"  Std Dev: {df[col].std():.2f}")
    print(f"  Range: {df[col].min():.2f} - {df[col].max():.2f}")

# Categorical features frequency
print("\n6. Categorical Features Frequency:")
categorical_cols = ['ContractType', 'InternetService', 'PaymentMethod', 'Gender']
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())

# Churn distribution
print("\n7. Churn Distribution:")
churn_counts = df['Churn'].value_counts()
churn_percentage = df['Churn'].value_counts(normalize=True) * 100
print(f"Churned: {churn_counts[1]} ({churn_percentage[1]:.1f}%)")
print(f"Not Churned: {churn_counts[0]} ({churn_percentage[0]:.1f}%)")


print("\n" + "="*50)
print("TASK 3: Tenure vs Churn Analysis")
print("="*50)

# Average tenure by churn status
tenure_by_churn = df.groupby('Churn')['Tenure'].agg(['mean', 'median', 'std'])
print("Tenure Statistics by Churn Status:")
print(tenure_by_churn)

# Detailed analysis
churned_tenure = df[df['Churn'] == 1]['Tenure']
non_churned_tenure = df[df['Churn'] == 0]['Tenure']

print(f"\nDetailed Analysis:")
print(f"Average tenure for churned customers: {churned_tenure.mean():.2f} months")
print(f"Average tenure for non-churned customers: {non_churned_tenure.mean():.2f} months")
print(f"Difference: {non_churned_tenure.mean() - churned_tenure.mean():.2f} months")

# Statistical test for significance
from scipy import stats
t_stat, p_value = stats.ttest_ind(churned_tenure, non_churned_tenure)
print(f"\nStatistical Test (t-test):")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")
print("The difference is statistically significant." if p_value < 0.05 else "The difference is not statistically significant.")


print("\n" + "="*50)
print("TASK 4: Creating Visualizations")
print("="*50)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Customer Churn Analysis Dashboard', fontsize=16, fontweight='bold')

# Visualization 1: Distribution of Monthly Charges by Contract Type (KDE Plot)
print("\nCreating Visualization 1: Monthly Charges Distribution by Contract Type...")
plt.sca(axes[0, 0])
for contract in contract_types:
    subset = df[df['ContractType'] == contract]['MonthlyCharges']
    sns.kdeplot(subset, label=contract, fill=True, alpha=0.6)

axes[0, 0].set_title('Distribution of Monthly Charges by Contract Type', fontweight='bold')
axes[0, 0].set_xlabel('Monthly Charges ($)')
axes[0, 0].set_ylabel('Density')
axes[0, 0].legend(title='Contract Type')
axes[0, 0].grid(True, alpha=0.3)

# Visualization 2: Churn Rate by Internet Service Type (Bar Chart)
print("Creating Visualization 2: Churn Rate by Internet Service Type...")
plt.sca(axes[0, 1])
churn_by_internet = df.groupby('InternetService')['Churn'].mean() * 100
bars = churn_by_internet.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen'], edgecolor='black')

axes[0, 1].set_title('Churn Rate by Internet Service Type', fontweight='bold')
axes[0, 1].set_xlabel('Internet Service Type')
axes[0, 1].set_ylabel('Churn Rate (%)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Add value labels on bars
for i, v in enumerate(churn_by_internet):
    axes[0, 1].text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')

# Visualization 3: Tenure Distribution by Churn Status (Additional)
plt.sca(axes[1, 0])
sns.boxplot(x='Churn', y='Tenure', data=df, palette=['lightgreen', 'lightcoral'])
axes[1, 0].set_title('Tenure Distribution by Churn Status', fontweight='bold')
axes[1, 0].set_xlabel('Churn Status (0 = No, 1 = Yes)')
axes[1, 0].set_ylabel('Tenure (Months)')

# Visualization 4: Churn Rate by Contract Type (Additional)
plt.sca(axes[1, 1])
churn_by_contract = df.groupby('ContractType')['Churn'].mean() * 100
bars = churn_by_contract.plot(kind='bar', color=['lightcoral', 'lightblue', 'lightgreen'], edgecolor='black')

axes[1, 1].set_title('Churn Rate by Contract Type', fontweight='bold')
axes[1, 1].set_xlabel('Contract Type')
axes[1, 1].set_ylabel('Churn Rate (%)')
axes[1, 1].tick_params(axis='x', rotation=45)

# Add value labels on bars
for i, v in enumerate(churn_by_contract):
    axes[1, 1].text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

print("All visualizations created successfully!")

# =============================================================================
# Additional Analysis and Summary Statistics
# =============================================================================
print("\n" + "="*50)
print("ADDITIONAL ANALYSIS")
print("="*50)

# Correlation analysis
print("\nCorrelation Matrix (Numerical Features):")
correlation_matrix = df[numerical_cols + ['Churn']].corr()
print(correlation_matrix['Churn'].sort_values(ascending=False))

# Churn rates by different categories
print("\nChurn Rates by Category:")
for col in categorical_cols:
    churn_rates = df.groupby(col)['Churn'].mean() * 100
    print(f"\n{col}:")
    for category, rate in churn_rates.items():
        print(f"  {category}: {rate:.1f}%")


print("\n" + "="*70)
print("TEXT-BASED ANALYSIS SUMMARY")
print("="*70)