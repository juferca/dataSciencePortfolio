# Marathon Performance Prediction

## Overview

This project analyzes 2024 NYC Marathon results to identify factors associated with marathon performance and evaluate machine learning models for predicting runner outcomes.

The analysis explores relationships between age, race experience, gender, pace, and age-graded performance metrics. Multiple predictive models were developed and compared to determine which approach produced the most accurate predictions.

## Business Problem

Understanding the factors that influence marathon performance can help athletes, coaches, and sports analysts better evaluate runner performance and identify meaningful predictors of race outcomes.

The goal of this project was to:

- Explore marathon runner characteristics.
- Identify correlations between performance variables.
- Predict marathon finishing performance using machine learning.
- Compare model effectiveness.

## Dataset

Dataset: NYC Marathon Results 2024

Features include:

- Age.
- Gender.
- Country.
- Race Count.
- Overall Place.
- Overall Time.
- Pace.
- Age Grade Percent.

Dataset Size:

- 55,524 runners.
- 17 variables.

### Dataset Sources

Hovde, J. (2024, November). *Data Is Plural reader Joe Hovde has scraped the results of the 2024 marathon into a downloadable spreadsheet. Data Is Plural.*

https://docs.google.com/spreadsheets/d/1O_zxndHKhKMIfJ9e7_M5L7b4F3S__d1nVnUS8iZn8yE/edit?gid=823797431#gid=823797431

Hovde, J. (2024). *2024 Marathon Results [Google Sheets].*

https://docs.google.com/spreadsheets/d/1O_zxndHKhKMIfJ9e7_M5L7b4F3S__d1nVnUS8iZn8yE/edit?gid=0#gid=0

## Data Preparation

Key preprocessing steps included:

- Handling missing values.
- Encoding gender variables.
- Converting time fields to numeric format.
- Converting pace to minutes-per-mile values.
- Feature selection and scaling.

## Exploratory Analysis

The project examined:

- Age distribution.
- Race experience distribution.
- Gender distribution.
- Marathon finishing time distribution.
- Correlation analysis.

Key findings:

- Age showed a weak positive relationship with finishing time.
- Race count showed a weak relationship with performance.
- Pace was the strongest predictor of marathon finishing time.
- Age-grade percent was strongly associated with performance.

## Models Evaluated

### Linear Regression

R² = 0.8586

### Random Forest

R² = 0.9244

### Gradient Boosting

R² = 0.9380

### Neural Network

R² = 0.9285

## Results

Gradient Boosting produced the best overall performance with the highest R² score.

The analysis found that:

- Pace is the strongest predictor of marathon performance.
- Age-grade percent significantly improves prediction accuracy.
- Ensemble models outperformed Linear Regression.

## Technologies Used

- Python.
- Pandas.
- NumPy.
- Matplotlib.
- Seaborn.
- Scikit-learn.
- TensorFlow / Keras.

## Files

| File                                                     | Description                 |
|----------------------------------------------------------|-----------------------------|
| Marathon_Performance_Analysis.ipynb                      | Main project notebook       |
| Marathon_Performance_Prediction.pdf                      | Project report and analysis |
| NYC Marathon Results, 2024 - Marathon Runner Results.csv | Dataset                     |
| README.md                                                | Project documentation       |

## Future Improvements

- Incorporate weather and course-condition data.
- Explore additional ensemble models.
- Develop runner performance forecasting tools.
- Create interactive dashboards for marathon analytics.
- Test advanced deep learning approaches.