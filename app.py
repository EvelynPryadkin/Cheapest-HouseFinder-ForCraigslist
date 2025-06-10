from flask import Flask, render_template, request
from scraper.craigslist import get_listings

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    listings = []
    city = "newyork"
    max_price = 1000

    if request.method == 'POST':
        city = request.form.get('city', 'newyork')
        max_price = int(request.form.get('max_price', 1000))
        listings = get_listings(city=city, max_price=max_price)

    return render_template('results.html', listings=listings, city=city, max_price=max_price)

if __name__ == '__main__':
    app.run(debug=True)
