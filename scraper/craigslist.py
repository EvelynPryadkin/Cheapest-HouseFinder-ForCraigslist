import requests
from bs4 import BeautifulSoup
import re

def get_listings(city='newyork', max_price=1000):
    url = f"https://{city}.craigslist.org/search/apa?max_price={max_price}&availabilityMode=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    print(f"Requesting URL: {url}")
    response = requests.get(url, headers=headers)
    print(f"Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('li', class_='cl-static-search-result')
    print(f"Found {len(results)} result(s)")

    listings = []

    for post in results:
        link_tag = post.find('a')
        title_tag = post.find('div', class_='title')
        price_tag = post.find('div', class_='price')

        if link_tag and title_tag and price_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            craigslist_price = price_tag.get_text(strip=True)


            clean_title = title.replace("o", "0")
            match = re.search(r"\$\d{3,5}", clean_title)


            if craigslist_price in ["$1", "$2", "$3", "$30", "$250", "$3", "$18", "$24"]:
                final_price = match.group(0) if match else craigslist_price
            else:
                final_price = craigslist_price

            listings.append({
                'title': title,
                'price': final_price,
                'link': link
            })

    return listings
