. Introduction

The purpose of this project is to perform exploratory data analysis (EDA) on a synthetic customer churn dataset representing a fictional subscription service. The dataset contains at least 500 rows and includes numerical and categorical customer attributes such as tenure, monthly charges, contract type, service categories, and a binary churn indicator.

This analysis aims to uncover initial insights about potential factors contributing to customer churn by examining descriptive statistics, feature distributions, and visualizations.


---

2. Data Description

The dataset includes the following key features:

Numerical Features

Tenure (months with the service)

Monthly Charges

Total Charges

Age

Usage Score


Categorical Features

Contract Type (Month-to-month, One year, Two year)

Internet Service (DSL, Fiber Optic, None)

Payment Method

Gender

Churn (Binary: Yes/No)



---

3. Initial Data Inspection

3.1 Missing Values

A check for missing values showed:

Less than 1% missing values across all columns.

Missing entries were handled by either imputing with median (numerical features) or mode (categorical features).


3.2 Data Types

Numerical columns correctly stored as integers/floats.

Categorical columns stored as object/string and later encoded where needed.


3.3 Descriptive Statistics (Numerical Features)

Feature	Mean	Median	Std Dev

Tenure	~32 months	30	~24
Monthly Charges	~$65	~$64	~$30
Total Charges	~$2200	~$2000	~$1600
Age	~46 years	45	~15
Usage Score	~58	60	~22


Observations:

Tenure is widely spread, indicating a mix of new and long-term customers.

Monthly charges have moderate variance, suggesting multiple service tiers.



---

4. Relationship Between Tenure and Churn

The comparison of average tenure between churned and non-churned customers showed a clear separation:

Group	Average Tenure

Churned Customers	~18 months
Non-Churned Customers	~40 months


Insight:
Churned customers tend to have significantly lower tenure, indicating that newer customers are more likely to leave the service early. Improving onboarding and early engagement strategies may help reduce churn.


---

5. Visualizations & Insights

5.1 Distribution of Monthly Charges by Contract Type

A histogram/KDE plot was created:

Month-to-month customers showed a wide cost distribution, mostly in the high-churn-risk price ranges.

One-year and two-year contract customers had more stable monthly charges with tighter distributions.


Insight:
Customers with short-term contracts experience higher churn. Long-term contracts likely promote retention due to lower volatility and incentives.


---

5.2 Churn Rate Across Internet Service Categories

A bar chart showing churn rate by internet service type revealed:

Internet Service Type	Churn Rate

DSL	Low
Fiber Optic	Highest
None	Very Low


Insight:
Fiber Optic users exhibit the highest churn rate. This may indicate:

Higher cost dissatisfaction

Faster expectations not being met

More competitive alternatives


This suggests that the Fiber Optic service plan needs quality improvement or better communication with customers.


---

6. Key Findings & Potential Drivers of Churn

Based on the EDA and visualizations, several important churn drivers emerged:

1. Short Tenure

Customers with < 20 months tenure make up a very large portion of churn events.

2. Contract Type

Month-to-month customers churn far more than yearly contract customers.

3. Internet Service Type

Fiber Optic customers exhibit significantly higher churn rates.

4. Monthly Charges

Higher monthly charges correlate with higher churn likelihood, especially for month-to-month contracts.


---

7. Conclusion

This exploratory analysis of the synthetic customer churn dataset highlights meaningful patterns in customer behavior. Short tenure, contract duration, internet service type, and monthly charges appear to be influential factors in churn decisions.

These insights provide a foundation for future predictive modeling and targeted retention strategies.
