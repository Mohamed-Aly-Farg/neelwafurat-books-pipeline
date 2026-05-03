import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import re
import sqlite3

# Configuration & Globals
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
BASE_URL = "https://www.neelwafurat.com/browsebycat.aspx?ddmSubject=26&search=books"
DATA_FOLDER = 'data'


def get_book_details(book_url):
    """
    Navigates to a specific book page and extracts detailed information.
    Includes error handling for missing elements.
    """
    try:
        response = requests.get(book_url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, 'lxml')

        # Extract title and author with fallback
        try:
            details_container = soup.find(
                "div", {"class": "col-xs-12 col-s-12 col-md-6 col-lg-6-5"})
            title = details_container.find(
                'h1', {'class': 'p-title'}).text.strip()
            author = details_container.find('a').text.strip()
        except AttributeError:
            title, author = "N/A", "N/A"

        # Extract publication date
        try:
            info_date = soup.find('div', {'class': "p-info p-format"})
            date_of_pub = info_date.contents[1].strip() if info_date else "N/A"
        except (AttributeError, IndexError):
            date_of_pub = "N/A"

        # Extract publisher
        try:
            publisher = soup.find('span', {'class': "bvendor"}).text.strip()
        except AttributeError:
            publisher = "N/A"

        # Extract price and handle different price tags
        try:
            price_box = soup.find("div", {"class": "payment-box"})
            price_tag = price_box.find('b', {'class': 'ourprice'})
            price = price_tag.text.strip() if price_tag else "0"
        except AttributeError:
            price = "0"

        return {
            'title': title,
            'author': author,
            'date_of_publication': date_of_pub,
            'publisher': publisher,
            'price_raw': price
        }
    except Exception as e:
        print(f"Error scraping {book_url}: {e}")
        return None


def save_to_sql(df):
    """
    Exports the cleaned DataFrame to a local SQLite database.
    """
    try:
        db_path = os.path.join(DATA_FOLDER, 'books_database.db')
        conn = sqlite3.connect(db_path)
        # Replaces the table if it already exists
        df.to_sql('books', conn, if_exists='replace', index=False)
        conn.close()
        print(f"✅ Data successfully exported to SQL Database: {db_path}")
    except Exception as e:
        print(f"❌ SQL Export Error: {e}")


def clean_and_process_data(raw_data_list):
    """
    Converts raw list to Pandas DataFrame, cleans numerical values, 
    and triggers export functions.
    """
    if not raw_data_list:
        print("No data collected!")
        return

    df = pd.DataFrame(raw_data_list)

    # Helper function to extract numeric price using Regex
    def parse_price(price_str):
        if pd.isna(price_str) or price_str == "0":
            return 0.0
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", str(price_str))
        return float(numbers[0]) if numbers else 0.0

    # Data Cleaning pipeline
    df['price_numeric'] = df['price_raw'].apply(parse_price)
    df['title'] = df['title'].str.strip()
    df['author'] = df['author'].str.strip()

    # Save to CSV
    csv_path = os.path.join(DATA_FOLDER, 'cleaned_books.csv')
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    print("\n" + "="*40)
    print("DATA SCRAPING SUMMARY")
    print("="*40)
    print(f"Total Records: {len(df)}")

    # Save to SQL Database
    save_to_sql(df)


def main():
    # Create data directory if it doesn't exist
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    print("--- Starting Neelwafurat Web Scraper ---")
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book containers on the main page
    book_containers = soup.find_all(
        'div', {'class': 'col-xs-6 col-s-4 col-lg-3 col-xxl-3 col-3xl-2'})

    results = []

    # Limit to first 10 for testing; remove indexing [:10] for full scrape
    for container in book_containers[:10]:
        link_tag = container.find('div', {'class': 'pro-info'}).find('a')
        book_link = link_tag['href']

        print(f"Processing: {book_link}")
        book_data = get_book_details(book_link)

        if book_data:
            results.append(book_data)

        # Respectful scraping: delay between requests
        time.sleep(1)

    # Process, Clean, and Store Data
    clean_and_process_data(results)
    print("--- Process Completed Successfully ---")


if __name__ == "__main__":
    main()
