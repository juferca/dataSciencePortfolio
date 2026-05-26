# Weather Forecast Python

## Overview

This project analyzes weather data from the [OpenWeatherMap API](http://openweathermap.org/api) using Python. The program allows users to search for weather information in U.S. cities either by city name or zip code. The goal of the project is to demonstrate how APIs, user input validation, error handling, and data processing can be combined into a practical real-world application.

##Business Problem

Many users want quick access to accurate weather information without navigating through websites or mobile apps. This project provides a command-line solution that retrieves live weather data directly from an external API. It also improves usability by allowing searches through both city names and zip codes while supporting multiple temperature scales.

## Data

The program retrieves live weather and geolocation data from the OpenWeatherMap API. The data includes:

- Current temperature.
- Feels-like temperature.
- Minimum and maximum temperatures.
- Humidity.
- Atmospheric pressure.
- Weather conditions.
- Geographic coordinates.
- City and state information.

## Data Preparation

The project performs several preparation and validation steps before displaying weather information:

- Validates user input for city names and zip codes.
- Ensures zip codes are exactly five digits.
- Converts temperature values from Kelvin into Celsius or Fahrenheit when selected by the user.
- Uses geolocation endpoints to retrieve latitude and longitude data before requesting weather information.
- Verifies API responses before processing the data.

## Methods

The project uses several programming and data handling techniques, including:

- API requests using the Python requests library.
- JSON response processing.
- Error handling using try and except statements.
- User input validation.
- Functions for modular programming.
- Temperature conversion calculations.
- Geolocation and reverse geolocation API calls.

## Program Features

The program includes several important features:

### Search by City

Users can search by city name. If multiple cities share the same name, the program displays up to five matching locations so the user can select the correct city.

### Search by Zip Code

Users can also search by zip code, allowing faster access to weather information for a specific area.

### Temperature Conversion

The program allows users to display temperatures in:

- Kelvin.
- Celsius.
- Fahrenheit.

### Error Handling

The project includes exception handling for:

- HTTP errors.
- Connection errors.
- Invalid user input.
- Missing API responses.

## Results

The program successfully retrieves and displays live weather information for U.S. cities. The application demonstrates:

- Successful integration with an external API.
- Proper handling of user input and errors.
- Data extraction and formatting from JSON responses.
- Accurate temperature conversions across multiple scales.
- Improved user experience through location selection and validation.

## Key Insights Learned

Several important programming concepts were learned and applied during this project:

- APIs can be used to retrieve real-time external data.
- JSON data structures can be parsed and transformed into readable outputs.
- Error handling is critical when working with external services.
- Breaking programs into functions improves readability and maintenance.
- User validation helps prevent crashes and improves reliability.
- Geolocation APIs can improve search flexibility and accuracy.

## Challenges

Some challenges encountered during development included:

- Handling multiple cities with the same name.
- Managing API errors and connection issues.
- Validating user input properly.
- Converting temperatures correctly between scales.
- Working with nested JSON responses from the API.

## Limitations

The project has several limitations:

- Only supports U.S. cities and zip codes.
- Requires internet access and a valid API key.
- Displays only current weather conditions.
- The application runs in a command-line environment without a graphical interface.

Future Work

## Future improvements could include:

- Adding a multi-day weather forecast.
- Supporting international locations.
- Creating a graphical user interface (GUI).
- Saving weather search history.
- Adding severe weather alerts.
- Improving output formatting with tables or visualizations.

## Conclusion

This project demonstrates how Python can be used to build a practical weather application using real-time API data. The program combines user interaction, data retrieval, validation, error handling, and temperature conversions into a functional command-line tool. Overall, the project strengthened understanding of APIs, Python programming structure, and working with live external data sources.
