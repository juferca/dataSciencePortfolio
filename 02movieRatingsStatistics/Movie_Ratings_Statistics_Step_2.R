# Assignment: Final Project Step 2
# Name: Caballero, Juan
# Date: 2024-08-05


# Dataset obtained from: https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset


# Set working directory.
setwd("C:/Users/Juan Caballero/Desktop/dataSciencePortfolio/02movieRatingsStatistics")

# Load libraries needed.
library(readxl)
library(dplyr)
library(tidyr)
library(ggplot2)


# IMPORTING DATA.
# I have two file formats, .csv and .xlsx. Importing .xlsx (slower to read) to main original data types.
# rotten_tomatoes_df <- read.csv("rotten_tomatoes_movies.csv")
rotten_tomatoes_df <- read_excel("rotten_tomatoes_movies.xlsx")

summary(rotten_tomatoes_df)


# DATA PREPARATION AND CLEANING.
# Check for missing values.
sum(is.na(rotten_tomatoes_df$tomatometer_rating))
sum(is.na(rotten_tomatoes_df$audience_rating))
sum(is.na(rotten_tomatoes_df$original_release_date))

# Drop rows with missing critic or audience ratings.
cleaned_rotten_tomatoes_data <- rotten_tomatoes_df %>% drop_na(tomatometer_rating, audience_rating, original_release_date)

# Select relevant columns
columns_selected <- c('movie_title', 'content_rating', 'genres', 'directors', 'actors', 'original_release_date', 'runtime', 'production_company',  'tomatometer_rating', 
                      'audience_rating')
cleaned_rotten_tomatoes_data <- cleaned_rotten_tomatoes_data %>% select(all_of(columns_selected))

# Extract year from release date
cleaned_rotten_tomatoes_data <- cleaned_rotten_tomatoes_data %>%
  mutate(release_year = as.numeric(format(original_release_date, "%Y")))

# Create score discrepancy variable
cleaned_rotten_tomatoes_data <- cleaned_rotten_tomatoes_data %>%
  mutate(score_discrepancy = tomatometer_rating - audience_rating)


# DISPLAY FINAL CLEANED DATASET.
# Display structure of cleaned dataset
str(cleaned_rotten_tomatoes_data)

# Display summary of cleaned dataset
summary(cleaned_rotten_tomatoes_data)


# Aggregate the data by year to get mean critic and audience scores.
trend_data <- cleaned_rotten_tomatoes_data %>%
  group_by(release_year) %>%
  summarize(mean_critic_score = mean(tomatometer_rating, na.rm = TRUE),
            mean_audience_score = mean(audience_rating, na.rm = TRUE))


# Plot trends in critic vs. audience scores over time.
ggplot(trend_data, aes(x = release_year)) +
  geom_line(aes(y = mean_critic_score, color = "Critic Score"), linewidth = 1) +
  geom_line(aes(y = mean_audience_score, color = "Audience Score"), linewidth = 1) +
  labs(title = "Trends in Critic vs. Audience Scores Over Time",
       x = "Year of Release",
       y = "Mean Score",
       color = "Score Type") +
  scale_color_manual(values = c("Critic Score" = "blue", "Audience Score" = "red")) +
  theme_minimal()


# Plot trend lines
ggplot(trend_data, aes(x = release_year)) +
  geom_smooth(aes(y = mean_critic_score, color = "Critic Score"), method = "loess", se = FALSE) +
  geom_smooth(aes(y = mean_audience_score, color = "Audience Score"), 
              method = "loess", se = FALSE) +
  labs(title = "Trends in Critic vs. Audience Scores Over Time",
       x = "Year of Release",
       y = "Mean Score",
       color = "Score Type") +
  scale_color_manual(values = c("Critic Score" = "blue", "Audience Score" = "red")) +
  theme_minimal()

# Plot scatter plots.
ggplot(trend_data, aes(x = release_year)) +
  geom_point(aes(y = mean_critic_score, color = "Critic Score"), size = 2) +
  geom_point(aes(y = mean_audience_score, color = "Audience Score"), size = 2) + 
  labs(title = "Trends in Critic vs. Audience Scores Over Time", x = "Year of Release", 
       y = "Mean Score", color = "Score Type") + 
  scale_color_manual(values = c("Critic Score" = "blue", "Audience Score" = "red")) + theme_minimal()


# Plot scatter plots with trend lines
ggplot(trend_data, aes(x = release_year)) +
  geom_point(aes(y = mean_critic_score, color = "Critic Score"), size = 2) +
  geom_point(aes(y = mean_audience_score, color = "Audience Score"), size = 2) +
  geom_smooth(aes(y = mean_critic_score, color = "Critic Score"), method = "loess", se = FALSE) +
  geom_smooth(aes(y = mean_audience_score, color = "Audience Score"), method = "loess", se = FALSE) +
  labs(title = "Trends in Critic vs. Audience Scores Over Time",
       x = "Year of Release",
       y = "Mean Score",
       color = "Score Type") +
  scale_color_manual(values = c("Critic Score" = "blue", "Audience Score" = "red")) +
  theme_minimal()
