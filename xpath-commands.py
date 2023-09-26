#xpath
>>> from selenium.webdriver import Chrome
>>> from selenium.webdriver.chrome.service import Service
>>> from selenium.webdriver.chrome.options import Options
>>> from webdriver_manager.chrome import ChromeDriverManager
>>> url = "https://books.toscrape.com/"
>>> chrome_options = Options()
>>> chrome_options.add_experimental_option("detach", True)
driver = Chrome(service=Service((ChromeDriverManager().install()),options=chrome_options)

xpath = "//article[p[@class="start-rating One"]]//h3/a/@title | //article[p[@class="start-rating Two"]]//p[@class="price_color"]/text()"

results = driver.find_elements("xpath", 

#Facility to not program or code 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from element_manager import *
driver = webdriver.Chrome(ChromeDriverManager().install())
# to click on the element(Travel              ...) found
driver.find_element(By.XPATH,get_xpath(driver,'9Dhz6kmhnBiy9mR')).click()

#Cryptography-pass-strings
>>> import string
>>> password = "askdnask"
>>> upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
>>> length = len(password)
>>> print(length)
8

>>> import string
>>> password = "askdnask"
>>> upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
>>> length = len(password)
>>> print(length)
8
>>> chatacters = [upper_case]
>>> score = 0
>>> if length > 8:
...     score += 1
