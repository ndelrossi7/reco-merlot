import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


# url = 'https://www.vivino.com/explore?e=eJzLLbI11jNVy83MszU0UMtNrLA1MVBLrrQNDVZLBhIuagW2hmrpabZliUWZqSWJOWr5SbZFiSWZeenF8YllqUWJ6alq-bYpqcXJauUl0bFAxWDKCEIZQygTCGUOlTNRK7bNqwQAfzEoDA=='
# r = requests.get(url)
# print(r.content)

driver = webdriver.Chrome('/Users/nataliedelrossi/Downloads/chromedriver')

# driver.get('https://www.vivino.com/explore?e=eJzLLbI11jNVy83MszU0UMtNrLA1MVBLrrQNDVZLBhIuagW2hmrpabZliUWZqSWJOWr5SbZFiSWZeenF8YllqUWJ6alq-bYpqcXJauUl0bFAxWDKCEIZQygTCGUOlTNRK7bNqwQAfzEoDA==')
driver.get('https://www.vivino.com/explore?e=eJwNyTEOgCAQBMDfbI2F5Xb-wFibE09CImAOQuT32kwzyTghxUyHJC9n5-AHtxX-Z8Hzb7jYxaI2uVEOmrSYQ92lq0lQFJ5aPSrz-ADEhhoc')


# first pass at getting winery names - no scrolling
wines = driver.find_elements_by_css_selector("a.anchor__anchor--2QZvA")
# CSS selector found by inspecting site 
wineries = []
testing = []
for wine in wines:
    wineries.append(wine.find_elements_by_css_selector("span.vintageTitle__winery--2YoIr"))
    # appending all of the selenium element by css_selector
for i in wineries:
    if i:
        testing.append(i[0].text)
        # returned many empty lists, now appending the text properties of the selenium element we have

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# driver.close()

# driver.quit()
