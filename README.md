Please ignore a.py.


you may run the jupiter notebook

# Project: Seattle Events Scraper

## Overview

This project involves scraping events happening in Seattle from the [Visit Seattle](https://visitseattle.org/) website. The scraped data includes event details like name, date, location, type, and region. Additionally, the project utilizes external services to look up location information using [Nominatim](https://nominatim.openstreetmap.org/) and fetches weather data for the event location using the [National Weather Service API](https://www.weather.gov/documentation/services-web-api).

## Scraping Visit Seattle Events

### 1. Scraping List Page

- The script extracts event detail page URLs from the list page by parsing the `href` attribute of anchor tags (`<a>`).
- Pagination is implemented to scrape events from multiple pages (`https://visitseattle.org/events/page/{page_number}`).
- The extracted URLs are stored in a list.

```python
[
    "https://visitseattle.org/events/glen-teriyaki/",
    "https://visitseattle.org/events/glen-teriyaki/",
    "https://visitseattle.org/events/glen-teriyaki/",
    ...
    "https://visitseattle.org/events/glen-teriyaki/",
    "https://visitseattle.org/events/glen-teriyaki/",
    "https://visitseattle.org/events/glen-teriyaki/",
]
```

### 2. Scraping Detail Page

- The script loops through the extracted event detail page URLs.
- HTTP GET requests are made to fetch the HTML content of each detail page.
- Information such as name, date, location, type, and region is extracted.
- The data is stored in a CSV file named "events.csv".

## Location Lookup

- The script utilizes the [Nominatim API](https://nominatim.openstreetmap.org/) to look up location information based on the event addresses.

## Weather Information

- The project fetches weather data for the event location using the [National Weather Service API](https://www.weather.gov/documentation/services-web-api). The script considers daytime weather for the specified date.

## Data Storage

- The final dataset, including event details, location information, and weather data, is stored as a CSV file.

## Instructions for Running the Script

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Execute the script by running `python scrape_events.py`.

