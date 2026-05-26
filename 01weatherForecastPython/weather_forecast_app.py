import requests
from pprint import pprint

# Replace with your own OpenWeatherMap API key
api_key = 'your_api_key_here'


# Function to make an API request and handle potential errors.
def make_api_request(url):
    try:
        response = requests.get(url)
        # Raise an HTTPError for bad responses (4xx and 5xx).
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        pprint(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError as e:
        pprint(f"Connection error occurred: {e}")
    except Exception as e:
        pprint(f"An error occurred: {e}")
    return None


# Function to get weather information by city name.
def get_weather_by_city(city_name, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},US&limit=5&appid={api_key}"
    # Make API request to get location data for the city.
    data = make_api_request(url)
    if data:
        print("\nFound the following locations:")
        # Enumerate through the locations starting from 1.
        for item, location in enumerate(data, start=1):
            print(f"{item}. {location['name']}, {location['state']} - Lat: {location['lat']}, Lon: {location['lon']}")

        while True:
            try:
                location_choice = int(input("\nEnter the number of the location you want to get the weather for: ")) - 1
                # Check if the choice is within the valid range.
                if 0 <= location_choice < len(data):
                    selected_location = data[location_choice]
                    lat = selected_location['lat']
                    lon = selected_location['lon']
                    city = selected_location['name']
                    state = selected_location['state']
                    # Return the location data.
                    return lat, lon, city, state
                else:
                    print("\nInvalid choice. Please enter a number corresponding to the listed locations.")
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
    else:
        print(f"\nNo locations found for city: {city_name}")
        # Return None if no data is found.
        return None, None, None, None


# Function to convert temperature from Kelvin to the specified unit.
def convert_temperature(temp_k, unit):
    if unit == 'c':
        # Convert to Celsius.
        return temp_k - 273.15
    elif unit == 'f':
        # Convert to Fahrenheit.
        return (temp_k - 273.15) * 9/5 + 32
    else:
        # Return Kelvin.
        return temp_k


# Function to get weather information by zip code.
def get_weather_by_zip(zip_code, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={api_key}"
    # Make API request to get location data for the zip code.
    data = make_api_request(url)
    if data:
        lat = data['lat']
        lon = data['lon']
        reverse_geo_url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=5&appid={api_key}"
        # Make API request to get reverse geocoding data.
        reverse_geo_response = requests.get(reverse_geo_url)
        if reverse_geo_response.status_code == 200:
            reverse_geo_data = reverse_geo_response.json()
            if reverse_geo_data:
                # Get state from reverse geocoding data.
                state = reverse_geo_data[0].get('state', 'N/A')
            else:
                state = 'N/A'
        else:
            state = 'N/A'

        city = data['name']
        # Return the location data.
        return lat, lon, city, state
    else:
        print(f"\nNo location found for zip code: {zip_code}")
        # Return None if no data is found.
        return None, None, None, None


# Function to get and display weather data.
def get_and_display_weather(lat, lon, city, state, api_key, temp_scale):
    # Construct the URL for the weather API request using the latitude, longitude, and API key.
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    # Make API request to get weather data.
    weather_response = make_api_request(weather_url)

    if weather_response:
        # Extract temperature in Kelvin from the response.
        temp_k = weather_response['main']['temp']

        # Extract 'feels like' temperature in Kelvin from the response.
        feels_like_k = weather_response['main']['feels_like']

        # Extract minimum temperature in Kelvin from the response.
        temp_min_k = weather_response['main']['temp_min']

        # Extract maximum temperature in Kelvin from the response.
        temp_max_k = weather_response['main']['temp_max']

        # Extract atmospheric pressure from the response.
        pressure = weather_response['main']['pressure']

        # Extract humidity percentage from the response.
        humidity = weather_response['main']['humidity']

        # Extract main weather description from the response.
        main_weather = weather_response['weather'][0]['main']

        # Convert the extracted temperatures from Kelvin to the desired unit.
        temp_converted = convert_temperature(temp_k, temp_scale)
        feels_like_converted = convert_temperature(feels_like_k, temp_scale)
        temp_min_converted = convert_temperature(temp_min_k, temp_scale)
        temp_max_converted = convert_temperature(temp_max_k, temp_scale)

        # Print the weather information for the specified city and state
        print(f"\nWeather for {city}, {state}:")
        print(f"The current temperature is {temp_converted:.2f} degrees {temp_scale.capitalize()}.")
        print(f"Feels like: {feels_like_converted:.2f} degrees {temp_scale.capitalize()}.")
        print(f"Minimum temperature: {temp_min_converted:.2f} degrees {temp_scale.capitalize()}.")
        print(f"Maximum temperature: {temp_max_converted:.2f} degrees {temp_scale.capitalize()}.")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {main_weather}\n")
    else:
        # Print an error message if the weather data could not be retrieved.
        print("\nFailed to retrieve weather data from OpenWeatherMap API.")


def main():
    print("\nWelcome to the U.S Cities OpenWeather Program!")
    while True:
        # Prompt user for city or zip.
        while True:
            user_choice = input("\nWould you like to look up the weather by city or zip code? (Enter 'city' or 'zip'): "
                                ).strip().lower()
            if user_choice in ['city', 'zip']:
                break
            else:
                print("\nInvalid input. Please enter 'city' or 'zip'.")

        # Prompt user for temperature scale.
        while True:
            temp_scale = input("\nHow do you want the temperature displayed? (Enter 'K' for kelvin, 'C' for celsius, or"
                               " 'F' for fahrenheit): ").strip().lower()
            if temp_scale in ['k', 'c', 'f']:
                break
            else:
                print("\nInvalid input. Please enter 'K' for kelvin, 'C' for celsius, or 'F' for fahrenheit): ")

        # Get weather data by city.
        if user_choice == 'city':
            city_name = input("\nEnter the city name: ").strip().lower()
            lat, lon, city, state = get_weather_by_city(city_name, api_key)
            if lat is None or lon is None:
                continue
        # Get weather data by zip code.
        else:
            while True:
                zip_code = input("\nEnter the zip code: ").strip()
                if zip_code.isdigit() and len(zip_code) == 5:
                    break
                else:
                    print("\nInvalid input. Please enter a 5-digit zip code.")
            lat, lon, city, state = get_weather_by_zip(zip_code, api_key)
            if lat is None or lon is None:
                continue

        # Display weather data.
        if lat is not None and lon is not None:
            get_and_display_weather(lat, lon, city, state, api_key, temp_scale)

        # Prompt user for another search or exit the program.
        another_search = input("\nWould you like to search for another location? (y/n): ").strip().lower()
        if another_search != 'y':
            print("\nLeaving the program. Goodbye!")
            break


if __name__ == "__main__":
    main()
