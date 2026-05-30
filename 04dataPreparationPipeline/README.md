# Movie Analytics: Data Acquisition, Preparation, and Analysis

## Project Overview

This project combines data from multiple movie-related sources to explore relationships between movie ratings, reviews, and audience reception. The goal was to acquire, clean, transform, and integrate data from several sources before performing exploratory data analysis.

The project demonstrates the complete data preparation workflow, including data acquisition, web scraping, data cleaning, transformation, database storage, and analysis using Python.

## Project Objectives

- Acquire movie data from multiple sources.
- Collect additional movie information through web scraping.
- Clean and transform raw datasets.
- Integrate data from different sources into a unified dataset.
- Store and manage data using SQLite.
- Perform exploratory data analysis to identify trends and relationships.

## Data Sources

### Kaggle Dataset

Movie information including:

- Movie titles.
- Genres.
- Audience ratings.
- Tomatometer ratings.
- Audience counts.
- Critic review counts.

**Source:**

- Rotten Tomatoes Movies and Critic Reviews Dataset
- https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset

### OMDb API

Additional movie information including:

- Runtime.
- Awards.
- IMDb ratings.
- User ratings.
- Plot summaries.

**Source:**

- OMDb API
- https://www.omdbapi.com/

### Web Scraping Sources

Additional movie information was collected from:

- IMDb.
- Rotten Tomatoes.
- Wikipedia.

Sources:

- https://www.imdb.com/
- https://www.rottentomatoes.com/
- https://en.wikipedia.org/wiki/Lists_of_films

## Data Integration Strategy

The datasets were connected using common movie identifiers such as:

- Movie Title.
- IMDb ID.

The Kaggle dataset served as the primary source of movie information. Data collected from the OMDb API was matched using IMDb IDs when available. Additional information collected from IMDb and Rotten Tomatoes was merged using standardized movie titles.

Data cleaning and normalization techniques were applied to improve matching accuracy across sources.

## Project Workflow

### Milestone 1: Project Planning and Data Sources

Defined project objectives, selected data sources, identified dataset relationships, anticipated challenges, and documented ethical considerations.

### Milestone 2: Data Acquisition

Imported and explored raw movie datasets from multiple sources.

File:

- `Milestone_2_Movie_Data_Acquisition.ipynb`

### Milestone 3: Web Scraping and Data Collection

Collected additional movie information from IMDb and other online sources.

File:

- `Milestone_3_Web_Scraping_and_Data_Collection.ipynb`

### Milestone 4: Data Cleaning and Transformation

Performed:

- Missing value treatment.
- Data type conversions.
- Duplicate removal.
- Data standardization.
- Dataset integration.

File:

- `Milestone_4_Data_Cleaning_and_Transformation.ipynb`

### Milestone 5: Exploratory Data Analysis and Visualization

Analyzed the integrated dataset and created visualizations to identify patterns and relationships among movie characteristics and ratings.

File:

- `Milestone_5_Exploratory_Data_Analysis_and_Visualization.ipynb`

## Technologies Used

- Python.
- Pandas.
- NumPy.
- SQLite.
- Requests.
- BeautifulSoup.
- Matplotlib.
- Seaborn.
- Jupyter Notebook.

## Project Files

### Raw Data

- `rotten_tomatoes_movies.csv`
- `rotten_tomatoes_critic_reviews.csv`
- `IMDb Top 100 Movies November 3, 2024.xlsx`

### Cleaned Data

- `cleaned_movie_data2.csv`
- `rt_cleaned_movies_df.csv`
- `rt_cleaned_critic_reviews_df.csv`
- `cleaned_imdb_df.csv`

### Integrated Dataset

- `joined_movies_dataset.csv`

### Database

- `movies_database.db`

### Project Notebooks

- `Milestone_2_Movie_Data_Acquisition.ipynb`
- `Milestone_3_Web_Scraping_and_Data_Collection.ipynb`
- `Milestone_4_Data_Cleaning_and_Transformation.ipynb`
- `Milestone_5_Exploratory_Data_Analysis_and_Visualization.ipynb`

## Challenges

- Matching movie records across multiple data sources.
- Handling missing and inconsistent values.
- Maintaining data quality during dataset merges.
- Adapting to changes in website structures used for web scraping.
- Working within API rate limits.

## Ethical Considerations

This project uses publicly available movie data and follows responsible data collection practices.

Considerations include:

- Respecting website terms of service.
- Limiting API requests to avoid excessive usage.
- Acknowledging potential bias in audience and critic ratings.
- Understanding that online reviews may not represent all audiences equally.

## Future Improvements

- Expand analysis with additional movie datasets.
- Incorporate machine learning models for rating prediction.
- Perform sentiment analysis on critic reviews.
- Automate data collection pipelines.
- Develop interactive dashboards for visualization.