from scraper.craigslist import get_listings
import csv

# Run the scraper
listings = get_listings(city="newyork", max_price=1000)

print(f"\nFound {len(listings)} clean listings:\n")

# Preview in terminal
for listing in listings[:10]:
    print(f"{listing['price']} - {listing['title']}")
    print(f"{listing['link']}\n")

# --- Save to TXT ---
with open("listings.txt", "w", encoding="utf-8") as txt_file:
    for listing in listings:
        txt_file.write(f"{listing['price']} - {listing['title']}\n")
        txt_file.write(f"{listing['link']}\n\n")

print("listings.txt saved.")

# --- Save to CSV ---
with open("listings.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["price", "title", "link"])
    writer.writeheader()
    for listing in listings:
        writer.writerow(listing)

print("listings.csv saved.")

