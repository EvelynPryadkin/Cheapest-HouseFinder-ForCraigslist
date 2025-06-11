# 🏠 Cheapest Housing Finder for Craigslist

A simple web app built with **Python**, **Flask**, and **BeautifulSoup** that helps you find the cheapest rental listings on Craigslist by city and maximum price.

> 💖 Now featuring a pastel pink UI, friendly error handling, and cleaned-up price formatting!

---

## ✨ Features

- 🔎 Search by city (e.g., `newyork`, `chicago`) and set a max rent
- 📄 View clean, accurate listings with fixed price formatting
- 📁 Export results to `.txt` and `.csv` files
- 💅 Cute, responsive pastel-themed UI
- 🚫 Error handling for invalid city names or connection issues

---

## 🌐 Live Demo

🚀 [Live Demo](https://your-render-url.onrender.com)

---

## 🚀 How to Run the App

1. **Clone this repository**

```bash
git clone https://github.com/yourusername/CheapestHouseFinder.git
cd CheapestHouseFinder
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🗃 Project Structure

```
CheapestHouseFinder/
│
├── app.py                  # Flask app main file
├── scraper/
│   ├── __init__.py         # Init for module
│   └── craigslist.py       # Scraper logic
│
├── static/
│   └── style.css           # Pastel pink styling
│
├── templates/
│   └── results.html        # HTML with Jinja2 templating
│
├── .gitignore              # Ignores venv and other unneeded files
├── README.md               # This file
├── requirements.txt        # Required pip packages
├── listings.txt            # Exported text file (optional)
└── listings.csv            # Exported CSV file (optional)
```

---

## 🧠 Tech Stack

- Python 3
- Flask
- BeautifulSoup
- requests
- HTML/CSS (with custom pastel theme ✨)

---

## 🛠 Example Input

**City:** `newyork`  
**Max Price:** `1000`

The app returns a list of links like:

```
$950 – Private Room for Rent  
https://newyork.craigslist.org/...

$800 – Spacious Studio  
https://newyork.craigslist.org/...
```

---

## 🐞 Error Handling

If a user types an invalid city (e.g., `california`), the app will show:

```
⚠️ No listings found for your search. Try a different city or price.
```

And log the issue without crashing the server.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Evelyn Pryadkin**  
[GitHub Profile](https://github.com/yourusername)  
Computer Science Major @ Lawrence University  

