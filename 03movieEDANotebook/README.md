\# Movie Ratings Analysis



\## Overview



This project analyzes movie critic ratings and audience ratings using Rotten Tomatoes movie data. The goal of the analysis is to better understand how critics and audiences evaluate movies differently and identify patterns related to movie runtime, content ratings, release years, and overall movie reception.



The project was completed using Python, Jupyter Notebook, statistical analysis, and data visualization techniques.



\## Business Problem



Movie critics and audiences do not always agree when rating movies. Critics may focus more on storytelling, cinematography, originality, and technical quality, while audiences may prioritize entertainment value and personal enjoyment.



This project explores the relationship between critic scores and audience scores to identify trends, similarities, and differences in movie rating behavior.



\## Data



The dataset used in this project comes from the Rotten Tomatoes Movies and Critic Reviews Dataset available on Kaggle.



Dataset includes:



\* Movie titles

\* Genres

\* Directors

\* Actors

\* Content ratings

\* Release dates

\* Runtime

\* Production companies

\* Critic scores (Tomatometer)

\* Audience scores

\* Critic review counts

\* Audience review counts



Dataset Source:



https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset



\## Data Preparation



Several cleaning and preparation steps were performed before analysis:



\* Removed rows with missing values

\* Converted release dates into datetime format

\* Extracted release year from release dates

\* Selected variables relevant to the analysis

\* Encoded categorical variables for regression analysis

\* Removed incomplete records to improve statistical reliability



Selected variables included:



\* `tomatometer\_rating`

\* `audience\_rating`

\* `content\_rating`

\* `runtime`

\* `release\_year`



\## Methods



The project uses several statistical and exploratory analysis techniques, including:



\* Exploratory Data Analysis (EDA)

\* Histograms and distribution analysis

\* PMF (Probability Mass Function)

\* CDF (Cumulative Distribution Function)

\* Scatter plots

\* Correlation analysis

\* Hypothesis testing using t-tests

\* Multiple linear regression



Python libraries used include:



\* pandas

\* numpy

\* matplotlib

\* seaborn

\* scipy

\* statsmodels

\* scikit-learn



\## Visualizations



The project includes several visualizations to analyze rating behavior and movie characteristics, including:



\* Histograms

\* Scatter plots

\* PMF comparisons

\* CDF plots

\* Normal distribution fitting

\* Correlation visualizations



The visualizations help identify trends, outliers, and relationships between variables.



\## Results



Several important findings were identified during the analysis:



\* Audience ratings and critic ratings show a moderate positive correlation.

\* Runtime has a very weak relationship with critic ratings.

\* Critics and audiences generally rate movies similarly on average.

\* Audience ratings tend to be slightly more stable than critic ratings.

\* Some content ratings appear more frequently than others, with R-rated movies dominating the dataset.

\* Multiple linear regression showed that audience rating, runtime, and content rating all contributed significantly to predicting critic scores.



Regression analysis achieved an R-squared value of approximately 0.46, meaning the model explained a moderate portion of the variation in critic ratings.



\## Key Insights Learned



This project strengthened understanding of:



\* Data cleaning and preprocessing

\* Statistical distributions

\* Correlation vs causation

\* Hypothesis testing

\* Regression modeling

\* Data visualization

\* Exploratory data analysis

\* Working with real-world movie datasets



\## Challenges



Some challenges encountered during development included:



\* Handling missing values

\* Working with categorical variables

\* Interpreting statistical distributions

\* Managing multicollinearity in regression analysis

\* Identifying meaningful relationships between movie variables

\* Understanding non-linear relationships in the data



\## Limitations



The project has several limitations:



\* The dataset only includes movies available in the Rotten Tomatoes dataset.

\* Financial information such as budgets and box office revenue was not included.

\* Genre information was difficult to analyze because movies can belong to multiple genres.

\* Ratings may contain personal bias from both critics and audiences.

\* The regression model assumes mostly linear relationships between variables.



\## Future Work



Possible future improvements include:



\* Adding box office and budget data

\* Building machine learning prediction models

\* Predicting rating discrepancies between critics and audiences

\* Creating interactive dashboards

\* Performing genre-specific analysis

\* Analyzing streaming-era movies separately

\* Exploring non-linear regression techniques



\## Conclusion



This project demonstrates how statistical analysis and visualization techniques can be used to explore relationships between movie critic ratings and audience ratings.



The analysis highlights how factors such as audience perception, runtime, and content rating may influence critic scores while also showing that critics and audiences often share similar opinions overall.



Overall, the project strengthened practical experience with Python programming, statistical analysis, regression modeling, and exploratory data analysis using real-world movie data.



\## Files Included



\* `movieRatingsAnalysis.ipynb` — Jupyter Notebook containing the full analysis

\* `movieRatingsAnalysis.pdf` — Exported PDF version of the notebook

\* `README.md` — Project overview and documentation



