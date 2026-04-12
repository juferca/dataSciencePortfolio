# Retail Sales & Profit Prediction

## Overview
This project analyzes how discounts affect retail sales and profit. While discounts are often used to increase sales, they do not always lead to higher profits. The goal of this project is to better understand that relationship and use machine learning to predict outcomes.

## Business Problem
Retail companies frequently rely on discounts to drive sales, but excessive discounting can reduce profitability. This project explores how pricing strategies impact both revenue and profit.

## Data
The dataset used is the Superstore dataset from Kaggle. It includes:
- Sales.
- Profit.
- Discount.
- Quantity.
- Product categories.
- Order dates.

## Data Preparation
- Converted date fields to datetime format.
- Created new features:
  - Month.
  - Year.
  - Day of week.
  - High discount indicator.
- Verified no missing values.

## Methods
The project uses:
- Exploratory Data Analysis (EDA).
- Machine Learning models:
  - Linear Regression.
  - Random Forest.
  - Gradient Boosting.

## Results
- Higher discounts are associated with lower profits.
- Random Forest performed better than Linear Regression.
- Model performance was moderate, suggesting missing variables.

## Key Insight
Discounts can increase sales but often hurt profitability, especially above 20%.

## Limitations
- Limited dataset.
- Missing external factors (seasonality, promotions, etc.).
- Model accuracy is relatively low.

## Future Work
- Add more features (customer behavior, external data).
- Improve model accuracy.
- Test additional machine learning models.
