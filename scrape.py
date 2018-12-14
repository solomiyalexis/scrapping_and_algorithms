from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://spoon.com.ua/').text

soup = BeautifulSoup(source, 'html5lib')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'photo_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        photo = article.find('div', class_='entry-thumbnail').a.img['src']
    except Exception as e:
        photo = None

    print(photo)

    print()

    csv_writer.writerow([headline, summary, photo])

csv_file.close()