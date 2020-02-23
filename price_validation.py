#! python3
# price_validation.py - Logs in to explore.ms and fetches the Special Pricing data. Exports the data to Validation Sheet.


# Currently searches google with the argument provided. 
import sys, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Validating if argument was input
if len(sys.argv) < 2:
    print("Don't forget the argument!")
    sys.exit() 
argument = sys.argv[1]

# Selenemium accessing page

def find(css_selector): # Search webpage by css selector
    return browser.find_element_by_css_selector(css_selector)

browser = webdriver.Chrome()
current_url = browser.get('https://www.google.com/')
searchbox = find('input.gLFyf.gsfi')
search_button = find('input.gNO89b')
searchbox.send_keys(argument)
search_button.click()

# BeatifulSoup retrieving data from currentpage
current_url = browser.current_url
result = requests.get(str(current_url))
website_content = result.content
soup = BeautifulSoup(website_content, 'lxml')
result_links = soup.find_all('a')
for link in result_links:
    print(link.attrs['href'])
print('Search done!')
sys.exit()