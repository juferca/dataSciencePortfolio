# Movie Ratings Statistics

## Overview

This project analyzes the differences between movie critic ratings and audience ratings using Rotten Tomatoes data. The goal of the project is to better understand why critics and audiences sometimes disagree on movie quality and identify patterns related to genres, release years, directors, and movie popularity.

The project was completed using R, R Markdown, statistical analysis, and data visualization techniques.

## Business Problem

Movie critics and audiences often rate the same movie very differently. Critics may focus more on artistic quality, storytelling, or technical execution, while audiences may rate movies based on entertainment value and personal enjoyment.

This project explores the factors that may contribute to these differences and attempts to identify trends in critic and audience behavior.

## Data

The dataset used in this project comes from the Rotten Tomatoes Movies and Critic Reviews Dataset available on Kaggle.

Dataset includes:

* Movie titles.
* Genres.
* Directors.
* Actors.
* Content ratings.
* Release dates.
* Runtime.
* Production companies.
* Critic scores (Tomatometer).
* Audience scores.
* Critic review counts.
* Audience review counts.

Dataset Source:

https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset

## Data Preparation

Several data cleaning and preparation steps were performed before analysis:

* Removed rows with missing critic or audience ratings.
* Removed rows with missing release dates.
* Selected only relevant variables for analysis.
* Extracted release year from release date.
* Created a new variable called `score_discrepancy` to measure the difference between critic and audience scores.

## Methods

The project uses:

* Exploratory Data Analysis (EDA).
* Statistical summaries.
* Data visualization.
* Data grouping and aggregation.
* Trend analysis over time.

R packages used include:

* tidyverse
* ggplot2
* dplyr
* readr
* lubridate
* readxl

## Visualizations

The project includes several visualizations to analyze rating patterns, including:

* Line charts.
* Scatter plots.
* Trend lines.
* Score comparisons over time.

The analysis compares average critic and audience scores by movie release year to identify long-term trends and discrepancies.

## Results

Several important findings were identified during the analysis:

* Critics and audiences do not always rate movies similarly.
* Score discrepancies vary across different decades.
* Some genres appear to create larger rating gaps.
* Audience scores tend to remain more stable over time.
* Critic scores show stronger fluctuations across release years.
* Blockbuster films may create more disagreement between critics and audiences than independent films.

## Key Insights Learned

This project helped strengthen understanding of:

* Data cleaning and preparation in R.
* Working with large datasets.
* Statistical summaries.
* Data visualization using ggplot2.
* Feature engineering.
* Trend analysis.
* Using R Markdown for reproducible reports.

## Challenges

Some challenges encountered during the project included:

* Handling missing data.
* Working with movies assigned to multiple genres.
* Organizing large amounts of categorical data.
* Identifying meaningful patterns within rating discrepancies.
* Limited availability of financial movie data such as budgets and box office performance.

## Limitations

The project has several limitations:

* Dataset only includes movies through 2020.
* Budget and box office data were not included.
* Movies may belong to multiple genres simultaneously.
* Audience and critic reviews may contain bias.
* The project focuses mainly on exploratory statistical analysis.

## Future Work

Possible future improvements include:

* Adding movie budget and box office datasets.
* Applying machine learning models.
* Predicting score discrepancies.
* Building interactive dashboards.
* Expanding analysis by actor or director.
* Comparing streaming-era movies versus theatrical releases.

## Conclusion

This project demonstrates how statistical analysis and visualization techniques can be used to explore differences between critic and audience movie ratings. The analysis highlights how movie reception can vary depending on audience expectations, genres, release periods, and other factors.

Overall, the project strengthened practical experience with R programming, data cleaning, visualization, and exploratory analysis while providing insights into movie rating behavior.
