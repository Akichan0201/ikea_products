import time
import typer
import pandas as pd

from rich import print
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def create_browser(type_browser:str):
    #web driver option
    options = webdriver.ChromeOptions()
    
    # options.add_experimental_option('detach', True) #detach for debugging!
    options.add_experimental_option('detach', True)
    options.add_argument('--start-maximized')

    if type_browser == "headless":
        options.add_argument('--headless')
    
    #module with selenium
    Chrome_driver = webdriver.Chrome(options=options)

    return Chrome_driver

def get_page(Chrome_driver):
    time.sleep(2)
    
    Chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 1300);") #

    element = Chrome_driver.find_element(By.LINK_TEXT, 'Show more')

    if element:
        element.click()
    else:
        print("element is not found")


def get_sele(link:str = 'https://www.ikea.com/gb/en/cat/last-chance/', page:int = 1, type_browser: str = 'headless'):
    #module with selenium
    Chrome_driver = create_browser(type_browser)
    Chrome_driver.get(link)

    time.sleep(2)
    # accept cookies
    Chrome_driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

    # getting page
    for i in range(1, page):
        print(f'page {i} success')
        get_page(Chrome_driver) 

    time.sleep(3)
    # check result
    html = Chrome_driver.page_source
    div = extract_data(html)
    return div
    
def export_data(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, sheet_name='page 1', index=False)
    print('success')

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    #parsing title
    product = []
    div = soup.find_all('div', class_='plp-fragment-wrapper')

    for div_1 in div:
        #parsing link product
        link_product = div_1.find('a')['href']
        print(link_product)

        # parsing title
        span = div_1.find('span', class_='notranslate plp-price-module__product-name')
        span = span.text
        print(span)
        print('=======================================================================')

        #parsing price
        price_module = div_1.find('div', class_='plp-price-module__price')
        price = price_module.find('span', class_='plp-price__integer')
        price_decimals = price_module.find('span', class_='plp-price__decimal')        
        price = price.text 

        if price_decimals:
            price = price + price_decimals.text.strip()
        
        #parsing review
        review = div_1.find('div', class_='plp-mastercard__item plp-mastercard__price')
        review = review.find('button')
        
        if review:
            review = review.find('span',class_='plp-rating__label').text # tanpa ()
        else:
            review = 0

        dict = {
            'link product': link_product,
            'title': span,
            'price': price,
            'reviews': review
        }
        product.append(dict)
    export_data(product, 'Ikea_products.xlsx')

if __name__=='__main__':
    typer.run(get_sele)