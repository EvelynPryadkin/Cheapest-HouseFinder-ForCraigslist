# 🏡 Cheapest Housing Finder (Craigslist Edition)

A beautiful pastel-pink themed web app built with Flask and Python that helps you find the cheapest housing listings by city and price on Craigslist. Includes CSV and TXT export options and a cozy front-end design!

---

## 🌟 Features

- 🔎 Search by city name (e.g. `newyork`, `chicago`)
- 💰 Filter by maximum price
- 📄 Export listings to `.csv` and `.txt`
- 🎨 Soft pastel pink UI with gradients and cozy fonts
- 💻 Simple Flask backend and BeautifulSoup scraper

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/cheapest-housing-finder.git
cd cheapest-housing-finder
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```
CheapestHouseFinder/
├── app.py                 # Main Flask app
├── scraper/               # Craigslist scraping logic
│   ├── __init__.py
│   └── craigslist.py
├── static/
│   └── style.css          # Custom pastel theme
├── templates/
│   └── results.html       # HTML template
├── listings.csv           # Exported results (sample)
├── listings.txt           # Exported results (sample)
├── requirements.txt       # Pip dependencies
├── test_scraper.py        # For manual scraper testing
└── .gitignore             # Ignores venv and unnecessary files
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Future Ideas

- Switch to Zillow API via RapidAPI
- Add Google Maps support and image thumbnails
- Mobile-first responsive UI
- Bookmark/save listings
- Deploy with Render or PythonAnywhere

---

Made with 💖 by Evelyn Pryadkin
