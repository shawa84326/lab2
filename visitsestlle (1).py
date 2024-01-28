# -*- coding: utf-8 -*-
"""visitsestlle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z6iOXrE4J10T-H8EX4z0OAjLbZIDqRfZ
"""

!pip install -r requirements.txt
!pip install html2text
!pip install requests-html

import time

import requests

url = "https://visitseattle.org/events/page/1"

# Create -> POST
# Read   -> GET
# Update -> PUT
# Delete -> DELETE
#
# requests.post("https://concert.com/buy")
# requests.put("https://github.com/ianchen06")
# requests.delete("https://facebook.com/ianchen06/post/1")

res = requests.get(url)

# 200 -> OK
# 201 -> Created (after POST)
# 301 -> Moved Permanently
# 302
# 400 -> Bad Request (error from user)
# 404 -> Not Found (error from user)
# 500 -> Internal Server Error (error from server)
res.status_code

res.text

open("seattleevents.html", "w").write(res.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

selector = "div.search-result-preview > div > h3 > a"

a_eles = soup.select(selector)
a_eles

[x['href'] for x in a_eles]

import requests
from bs4 import BeautifulSoup

for url in ['https://visitseattle.org/events/kate-alice-marshall/', 'https://visitseattle.org/events/machine-head/', ...]:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract information from the HTML using BeautifulSoup
        # Example: print the title of the page
        title = soup.title.string.strip()
        print(f"Title of {url}: {title}")
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")



import requests
from bs4 import BeautifulSoup

def scrape_event_urls(url):
    event_urls = []

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract event URLs using the provided CSS selector
        selector = "div.search-result-preview > div > h3 > a"
        event_tags = soup.select(selector)
        event_urls.extend([tag['href'] for tag in event_tags])

        return event_urls
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Scraping event URLs from all pages
base_url = "https://visitseattle.org/events/page/"
total_pages = 41  # You mentioned 41 pages
all_event_urls = []

for page_number in range(1, total_pages + 1):
    url = f"{base_url}{page_number}"
    event_urls = scrape_event_urls(url)

    if event_urls:
        all_event_urls.extend(event_urls)

# Print the result
print(all_event_urls)

import requests
from bs4 import BeautifulSoup
import csv

def extract_event_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information from the HTML using BeautifulSoup
        name = soup.find('h1', class_='page-title').text.strip()
        date = soup.find("h4").find_all("span")[0].text.strip()
        location = soup.find("h4").find_all("span")[1].text.strip()
        event_type = soup.find_all("a", class_="button big medium black category")[0].text.strip()
        region = soup.find_all("a", class_="button big medium black category")[1].text.strip()

        # Store the details in a dictionary
        event_details = {
            'Name': name,
            'Date': date,
            'Location': location,
            'Type': event_type,
            'Region': region
        }

        print(f"Details for {name} ({url}):")
        print(f"  Date: {date}")
        print(f"  Location: {location}")
        print(f"  Type: {event_type}")
        print(f"  Region: {region}")
        print()

        return event_details

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# List of event URLs


all_event_details = []

# Extract details for each event URL
for url in all_event_urls:
    event_details = extract_event_details(url)
    if event_details:
        all_event_details.append(event_details)

# Store the details in a CSV file
csv_file_path = 'events.csv'
fields = ['Name', 'Date', 'Location', 'Type', 'Region']

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    # Write the header
    writer.writeheader()
    # Write the event details
    writer.writerows(all_event_details)

print(f"Event details stored in {csv_file_path}")

"""# Weather API"""

import requests

url = "https://api.weather.gov/points/39.7456,-97.0892"
res = requests.get(url)
res

res.text

point_dict = res.json()
point_dict

point_dict.keys()

forcast_url = point_dict['properties']['forecast']
forcast_url

res = requests.get(forcast_url)
res.json()

from logging import exception
def get_weathers(latitude, longitude, date):
  try:


        # Format coordinates without extra characters
        coordinates = f'{latitude},{longitude}'

        # Construct API URL
        api_url = f'https://api.weather.gov/points/{coordinates}'

        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        point_dict = response.json()
        point_dict.keys()
        forcast_url = point_dict['properties']['forecast']
        forcast_url
        response = requests.get(forcast_url)
        response.json()
        forecast_data = response.json()


        print(response.json())
        return response.json()

  except requests.exceptions.HTTPError as e:
        print(f"Error fetching weather data: {e}")
        return None
  except (KeyError, ValueError, TypeError) as e:
        print(f"Unexpected response format from weather API: {e}")
        return None
  except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

import requests
import json

def get_weather(latitude, longitude, date):
    try:
        # Format coordinates without extra characters
        coordinates = f'{latitude},{longitude}'

        # Construct API URL for the points endpoint
        api_url = f'https://api.weather.gov/points/{coordinates}'

        # Make request to points endpoint
        response = requests.get(api_url)
        response.raise_for_status()
        point_data = response.json()

        # Extract forecast URL from the points data
        forecast_url = point_data['properties']['forecast']

        # Make request to forecast endpoint
        response = requests.get(forecast_url)
        response.raise_for_status()
        forecast_data = response.json()

        # Extract the daytime forecast for the specified date
        periods = forecast_data.get('properties', {}).get('periods', [])
        is_daytime_values = []

        for period in periods:
            start_time = period.get('startTime', '')
            start_date = start_time.split('T')[0]

            # Print for debugging


            # Check if the period corresponds to the specified date
            if start_date == date:
                is_daytime_values.append(period.get('isDaytime', False))

        return daytime_values

    except requests.exceptions.HTTPError as e:
        print(f"Error fetching weather data: {e}")
        return None
    except (KeyError, ValueError, TypeError) as e:
        print(f"Unexpected response format from weather API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
#latitude = 47.6090191
#longitude = -122.32993774092222
#date = '2024-01-28'  # Specify the date in 'YYYY-MM-DD' format

#daytime_values = get_weather(latitude, longitude, date)
#print("Daytime Values:")
#print(daytime_values)

"""The weather API requres lat, lon information, but we only have the location name...

Let's use the OpenStreetMap API to get the lat, lon information from location name.

# OpenStreeetMap Geocoding API
"""

# location name to lat lon

# Option 1: just string manipulation
base_url = "https://nominatim.openstreetmap.org/search.php"
query_params_str = "?q=Wallingford%2C+Seattle&format=jsonv2"
ful_url = base_url + query_params_str

# Option 2: use dictionary to represent query params
#           use requests.get(url, params=query_params) to attach the query param dict
query_params = {
    "q": "Wallingford, Seattle",
    "format": "jsonv2"
}

res = requests.get(base_url, params=query_params)
res.json()

import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim  # Add this line
import csv
from datetime import datetime



# Function to get location coordinates using Nominatim
def get_location_coordinates(location):
  try:
    geolocator = Nominatim(user_agent="event_scraper")
    location_info = geolocator.geocode(location)
    if location_info:
        return location_info.latitude, location_info.longitude
    return None, None
  except Exception as e:
        print(f"An error occurred while getting location coordinates: {e}")
        return None, None

"""Now we have the lat, lon information for a location, we can use the Weather.gov API to get the weather information."""

# Store event details with location and weather in a CSV file
csv_file_path = 'events_with_location_and_weather.csv'
fields = ['Name', 'Date', 'Location', 'Type', 'Region', 'URL', 'Latitude', 'Longitude', 'Weather']
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for event_details in all_event_details:
        latitude, longitude = get_location_coordinates(event_details['Location'])

        weather = get_weather(latitude, longitude, event_details['Date'])
        print(weather)



        if latitude is not None and longitude is not None:


            writer.writerow({
                'Name': event_details['Name'],
                'Date': event_details['Date'],
                'Location': event_details['Location'],
                'Type': event_details['Type'],
                'Region': event_details['Region'],
                'Weather': weather,
                'Latitude': latitude,
                'Longitude': longitude,

            })
        else:
            print(f"Unable to get location coordinates for {event_details['Location']}")

print(f"Event details with location and weather stored in {csv_file_path}")

import requests
import json

def get_weather(latitude, longitude, date):
    try:
        # Format coordinates without extra characters
        coordinates = f'{latitude},{longitude}'

        # Construct API URL for the points endpoint
        api_url = f'https://api.weather.gov/points/{coordinates}'

        # Make request to points endpoint
        response = requests.get(api_url)
        response.raise_for_status()
        point_data = response.json()

        # Extract forecast URL from the points data
        forecast_url = point_data['properties']['forecast']

        # Make request to forecast endpoint
        response = requests.get(forecast_url)
        response.raise_for_status()
        forecast_data = response.json()

        # Extract the daytime forecast for the specified date
        periods = forecast_data.get('properties', {}).get('periods', [])
        is_daytime_values = []

        for period in periods:
            start_time = period.get('startTime', '')
            start_date = start_time.split('T')[0]

            # Print for debugging
            print(f"Checking period: {start_time}, Start Date: {start_date}")

            # Check if the period corresponds to the specified date
            if start_date == date:
                is_daytime_values.append(period.get('isDaytime', False))

        return is_daytime_values

    except requests.exceptions.HTTPError as e:
        print(f"Error fetching weather data: {e}")
        return None
    except (KeyError, ValueError, TypeError) as e:
        print(f"Unexpected response format from weather API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
latitude = 47.6090191
longitude = -122.32993774092222
date = '2024-01-28'  # Specify the date in 'YYYY-MM-DD' format

daytime_values = get_weather(latitude, longitude, date)
print("Daytime Values:")
print(daytime_values)