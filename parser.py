import csv
from datetime import datetime
from time import sleep
from random import random

import requests
from bs4 import BeautifulSoup

import db
from config import *


def converting_date(date_row):
    if 'ago' in date_row:
        return datetime.strftime(datetime.today(), "%d/%m/%Y")

    return date_row


def processing_price(price_row):
    if price_row[-1].isdigit():
        return float(price_row[1:].replace(',', '')), price_row[0]

    return None, None


def page_parser(page_number):
    url = get_url(page_number)
    res = requests.get(url=url, headers=headers)
    page = res.text

    soup = BeautifulSoup(page, 'html.parser')
    all_box = soup.find_all(class_='search-item')
    print(f"  Page {page_number} has {len(all_box)} items")

    items = []
    for box in all_box:
        item_id = box.get('data-listing-id')  # soup.find('div', attrs={'data-listing-id': item_id})
        image = box.find('img').get('data-src')
        title = box.find(class_='title').text.strip()
        date = converting_date(box.find(class_='date-posted').text.strip())
        location = box.find(class_='location').span.text.strip()
        beds = box.find(class_='bedrooms').text.strip().split('\n')[1].strip()
        description = ' '.join(box.find(class_='description').text.split())
        price, currency = processing_price(box.find(class_='price').text.strip())

        items.append((item_id, image, title, date, location, beds, description, price, currency))

    # Insert into MySQL database
    db.insert(items)

    # Insert into CSV sheet
    with open('data/data.csv', 'a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(items)


def main():
    # Prepare CSV-file
    with open('data/data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(('id', 'image', 'title', 'date', 'location', 'beds', 'description', 'price', 'currency'))

    # Prepare MySQL database
    db.create_db()
    db.create_table()

    for i in range(start_page, finish_page + 1):
        print(f"- Parsing page number {i}...")
        page_parser(i)
        print(f"+ Page number {i} successful parsed.\n")
        sleep(1 + 2 * random())

    # db.show()


if __name__ == '__main__':
    main()
