# 🧁 Dessert Recipe Scraper

## What It Does
Python web scraping project that collects dessert recipes from (https://www.janespatisserie.com/category/dessert/).  
It scrapes recipe titles, images url, ingredients, and instructions, then saves the data to a JSON file.

## Project Structure

| File | Description |
|------|-------------|
| `config.json` | Configuration file (URLs, delay, output file) |
| `desserts.json` | Output file with scraped data (created after running) |
| `main.log` | Log file (errors, scraping status) |
| `pp1.py` | Main Python scraper script |
| `requirements.txt` | List of required packages |
| `.gitignore`       | Specifies files/folders to ignore in git |
| `README.md` | Project description and usage instructions |

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## How to Run the Scraper
```bash
# 1. Clone The Repository
git clone <your-repo-link>
cd PP1

# 2. Create Virtual Environment (optional)
python3 -m venv venv
source venv/bin/activate

# 3. Install Required Packages
pip install -r requirements.txt

# 4. Adjust Configuration
Open config.json and update the values if needed:
{
  "start_url": "https://www.janespatisserie.com/category/dessert/",
  "base_url": "https://www.janespatisserie.com/category/dessert/page/{}/",
  "pages_to_scrape": 3,
  "delay_seconds": 1,
  "output_file": "desserts.json"
}

# Configuration Options:
start_url: URL of the first page to scrape.
base_url: Template URL for paginated pages (page 2, 3, etc.).
pages_to_scrape: Number of pages to scrape.
delay_seconds: Delay between requests to avoid overloading the server.
output_file: Where the results will be saved.

IMPORTANT: This scraper is adjusted to the structure of janespatisserie.com web site. Other websites may not work without code changes.

# 5. Run The Code
python pp1.py
```

## Output
Scraped data is saved in: desserts.json
Log messages (errors, progress) are saved in: main.log.

## Features
Scrapes data from multiple pages (pagination).
Goes in-depth to each recipe page (title, ingredients, instructions).
Customizable with config.json.
Logs errors and progress to main.log.
Clean UTF-8 encoded output.

## Requirements
pip install -r requirements.txt

## Main dependencies:
requests  
beautifulsoup4

**Author:** Darius  
**Purpose:** Educational use only
