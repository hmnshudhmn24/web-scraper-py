import requests
import sqlite3
from bs4 import BeautifulSoup

# Database setup
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS articles (title TEXT, link TEXT)''')
conn.commit()

def scrape_website(url):
    """Scrapes article titles and links from a website."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('h2')  # Modify selector as needed

        for article in articles:
            title = article.get_text(strip=True)
            link = article.find('a')['href'] if article.find('a') else 'No Link'

            # Store data in the database
            cursor.execute('INSERT INTO articles (title, link) VALUES (?, ?)', (title, link))
            conn.commit()

        print(f'Successfully scraped data from {url}')
    else:
        print(f'Failed to retrieve data from {url}, Status Code: {response.status_code}')

if __name__ == "__main__":
    website_url = input("Enter the website URL to scrape: ")
    scrape_website(website_url)
    conn.close()
    print("Scraping completed. Data stored in 'scraped_data.db'.")
