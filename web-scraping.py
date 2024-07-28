import requests
from bs4 import BeautifulSoup

def get_weather_info(city):
    # Format the city name for the URL
    formatted_city = city.replace(' ', '%20')

    # URL for weather information from the National Weather Service (NWS)
    url = f'https://forecast.weather.gov/MapClick.php?textField1=37.7749&textField2=-122.4194#.X9IcfhNKjOQ'  # Coordinates for San Francisco, CA

    # Make a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract weather information
    try:
        location = soup.find('h2', class_='panel-title').text.strip()
        temp = soup.find('p', class_='myforecast-current-lrg').text
        condition = soup.find('p', class_='myforecast-current').text

        # Print the extracted information
        print(f"Location: {location}")
        print(f"Temperature: {temp}")
        print(f"Condition: {condition}")
    
    except AttributeError as e:
        print("Could not extract some of the information.")
        print(e)

# Example usage
city = "San Francisco, CA"  # You can change this to any city you want
get_weather_info(city)
