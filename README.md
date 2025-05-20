# IKEA Product Scraper

A Python project for scraping product data from the IKEA website using Selenium, BeautifulSoup, and Pandas.

## STAR Summary

**Situation:** IKEA's website presents a large catalog of products, but accessing structured data is not straightforward.

**Task:** Create a scraper to extract product details such as names, prices, categories, and links for further use or analysis.

**Action:**  
- Used Selenium to automate browser interaction and handle dynamic loading  
- Parsed HTML content with BeautifulSoup to extract relevant product information  
- Processed and exported data using Pandas into a clean CSV format

**Result:**  
Generated a structured dataset of IKEA products that can be used for data analysis, reporting, or integration into other tools.

## Features

- Navigates dynamically loaded product pages with Selenium
- Extracts structured product data using BeautifulSoup
- Outputs results in CSV format with Pandas or you can export it with xlsx format

Let me know if you'd like a version that includes images or data preview examples too.

## How to Use

```bash
git clone https://github.com/Akichan0201/ikea_products.git
cd ikea_products
pip install -r requirements.txt
python ikea_scraper.py

