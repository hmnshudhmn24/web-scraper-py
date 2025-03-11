# Web Scraper

## Overview
A **Python-based Web Scraper** that extracts article titles and links from websites and stores them in an SQLite database.

## Features
- Scrapes **article titles and links** from a given website.
- Stores the extracted data in an **SQLite database**.
- Uses **BeautifulSoup** for web scraping.
- Supports **custom user-agent headers** to avoid blocking.

## Requirements
Install dependencies using:
```
pip install requests beautifulsoup4
```

## Usage
1. Run the script:
```
python web_scraper.py
```
2. Enter the website URL when prompted.
3. The scraped data will be stored in `scraped_data.db`.

## Notes
- Modify the `soup.find_all('h2')` selector based on the website's HTML structure.
- Ensure you comply with a website’s `robots.txt` policy before scraping.
