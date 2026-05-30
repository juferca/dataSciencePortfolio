# Childcare Cost Analysis

## Project Overview

This project analyzes childcare costs across the United States using data from the National Database of Childcare Prices. The analysis explores cost differences between states, counties, age groups, and urban versus rural communities.

The goal is to identify patterns in childcare affordability, understand regional disparities, and examine economic factors that may influence childcare expenses.

## Business Problem

Childcare costs represent a significant financial burden for many families. Costs vary substantially across geographic regions and population centers, making access to affordable childcare unequal across the country.

This project investigates:

- Which states have the highest and lowest childcare costs.
- Differences in infant, toddler, and preschool childcare expenses.
- Urban versus rural childcare cost disparities.
- Childcare cost trends from 2008 to 2018.
- Relationships between childcare costs and economic indicators such as unemployment and labor force participation.

## Dataset Information

### Source

National Database of Childcare Prices

Published by:

U.S. Department of Labor – Women's Bureau

https://www.dol.gov/agencies/wb/topics/featured-childcare

### Dataset Description

The dataset contains county-level childcare pricing information across the United States from 2008 through 2018.

Key characteristics:

- 34,567 observations.
- 227 variables.
- Coverage of all U.S. states and counties.
- Childcare prices for:
  - Infants.
  - Toddlers.
  - Preschool-aged children.
- Economic indicators including:
  - Unemployment rates.
  - Labor force participation rates.
  - Demographic information.

## Data Preparation

The following preprocessing steps were performed:

- Converted childcare cost fields from currency strings to numeric values.
- Handled missing values using median imputation for numeric variables.
- Filled missing categorical values with "Unknown".
- Aggregated childcare costs at county and state levels.
- Created Urban and Rural classifications based on county childcare cost distributions.

## Analysis Performed

### State-Level Cost Analysis

- Median childcare costs by state.
- Comparison of infant, toddler, and preschool expenses.

### County-Level Cost Analysis

- Most expensive counties.
- Least expensive counties.

### Urban vs Rural Analysis

- Cost comparison by geographic classification.
- State-level urban and rural breakdowns.

### Trend Analysis

- Childcare cost changes from 2008–2018.
- Cost growth patterns across selected states.

### Economic Factors

- Correlation analysis between:
  - Unemployment rates.
  - Labor force participation rates.
  - Childcare costs.

## Key Findings

- Infant care is consistently the most expensive childcare category.
- Urban areas generally have higher childcare costs than rural areas.
- Massachusetts, Connecticut, and Washington were among the most expensive states.
- Mississippi, South Dakota, and Kansas were among the least expensive states.
- Childcare costs increased over time across many states.
- Labor force participation showed a positive relationship with childcare costs.
- Unemployment rates showed a weak negative relationship with childcare costs.

## Tools Used

- Python.
- Pandas.
- NumPy.
- Matplotlib.
- Seaborn.
- Jupyter Notebook.