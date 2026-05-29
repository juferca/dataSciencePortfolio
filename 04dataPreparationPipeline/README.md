# Movie Analytics: Data Acquisition, Preparation, and Analysis

## Project Overview

This project combines data from multiple movie-related sources to explore relationships between movie ratings, reviews, and audience reception. The goal was to acquire, clean, transform, and integrate data from several sources before performing exploratory data analysis.

The project demonstrates the complete data preparation workflow, including data acquisition, web scraping, data cleaning, transformation, database storage, and analysis using Python.

## Project Objectives

* Acquire movie data from multiple sources.
* Collect additional movie information through web scraping.
* Clean and transform raw datasets.
* Integrate data from different sources into a unified dataset.
* Store and manage data using SQLite.
* Perform exploratory data analysis to identify trends and relationships.

## Data Sources

### Rotten Tomatoes Movies Dataset

Contains movie information including:

* Movie titles.
* Genres.
* Audience ratings.
* Tomatometer ratings.
* Audience counts.
* Critic review counts.

File:

* `rotten_tomatoes_movies.csv`

### Rotten Tomatoes Critic Reviews Dataset

Contains critic review information including:

* Critic names.
* Review scores.
* Review content.
* Associated movie information.

File:

* `rotten_tomatoes_critic_reviews.csv`

### IMDb Top Movies Data

Additional movie information collected from IMDb.

Files:

* `IMDb Top 100 Movies November 3, 2024.xlsx`
* `cleaned_imdb_df.csv`

### SQLite Database

Integrated project data stored in:

* `movies_database.db`

## Project Workflow

### Milestone 1: Project Planning and Data Sources

Defined project objectives, selected data sources, identified relationships between datasets, and documented anticipated challenges and ethical considerations.

File:

* `Milestone_1_Project_Planning_and_Data_Sources.docx`

### Milestone 2: Data Acquisition

Imported and explored raw movie datasets from multiple sources.

File:

* `Milestone_2_Movie_Data_Acquisition.ipynb`

### Milestone 3: Web Scraping and Data Collection

Collected additional movie information through web scraping and external sources.

File:

* `Milestone_3_Web_Scraping_and_Data_Collection.ipynb`

### Milestone 4: Data Cleaning and Transformation

Performed:

* Missing value treatment
* Data type conversions
* Duplicate removal
* Data standardization
* Dataset integration

File:

* `Milestone_4_Data_Cleaning_and_Transformation.ipynb`

### Milestone 5: Exploratory Data Analysis and Visualization

Analyzed the integrated dataset and created visualizations to identify patterns and relationships among movie characteristics and ratings.

File:

* `Milestone_5_Exploratory_Data_Analysis_and_Visualization.ipynb`

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Requests
* BeautifulSoup
* Matplotlib
* Seaborn
* Jupyter Notebook

## Project Files

### Raw Data

* `rotten_tomatoes_movies.csv`
* `rotten_tomatoes_critic_reviews.csv`
* `IMDb Top 100 Movies November 3, 2024.xlsx`

### Cleaned Data

* `cleaned_movie_data2.csv`
* `rt_cleaned_movies_df.csv`
* `rt_cleaned_critic_reviews_df.csv`
* `cleaned_imdb_df.csv`

### Integrated Dataset

* `joined_movies_dataset.csv`

### Database

* `movies_database.db`

### Project Notebooks

* `Milestone_2_Movie_Data_Acquisition.ipynb`
* `Milestone_3_Web_Scraping_and_Data_Collection.ipynb`
* `Milestone_4_Data_Cleaning_and_Transformation.ipynb`
* `Milestone_5_Exploratory_Data_Analysis_and_Visualization.ipynb`

## Key Challenges

* Matching movie records across multiple data sources.
* Handling missing and inconsistent values.
* Maintaining data quality during merges.
* Adapting to changes in website structures used for web scraping.
* Ensuring reproducible data preparation steps.

## Future Improvements

* Incorporate additional movie datasets.
* Expand analysis using machine learning models.
* Automate data collection pipelines.
* Include sentiment analysis of critic reviews.
* Develop interactive dashboards for visualization.
