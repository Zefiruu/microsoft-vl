#! python3
# price_validation.py - Logs in to explore.ms and fetches the Special Pricing data. Exports the data to Validation Sheet.


# Currently searches google with the argument provided. 
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find(css_selector):
    return driver.find_element_by_css_selector(css_selector)


if len(sys.argv) < 2:
    print("Don't forget the argument!")
    sys.exit() 

argument = sys.argv[1]

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
searchbox = find('input.gLFyf.gsfi')
search_button = find('input.gNO89b')
searchbox.send_keys(argument)
search_button.click()
print('Search done!')
sys.exit()