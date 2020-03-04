import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import math
import re
import time
import pickle

driver = webdriver.Chrome('/Users/nataliedelrossi/Downloads/chromedriver')

driver.get('https://www.vivino.com/explore?e=eJwNxEEKgCAUBcDbvGUo1fLtukG0jp-ZCKmhInn7msWEzHGYEXykVgjyclIwndsK87fgoYa72CR7W-VGOpil-ujKLs1mcRaJpy0GhbF_488agQ==')

# find total number of wines on the page so that we can caluclate number of scrolls
# xpath is giving description of what wines are displayed and how many
def get_wine_links(driver):
    """
    Takes in our driver and allows us to see how many wines we have and what rating and price range it is in.
    Then dynamically scrolls to the end of the page and saves every link for each wine.
    """
    print(driver.find_element_by_xpath("""//*[@id="explore-page-app"]/div/div/h2""").text)
    num_wines = int(re.search(r"(?<=Showing ).*?(?= wines)", driver.find_element_by_xpath("""//*[@id="explore-page-app"]/div/div/h2""").text).group(0))
    # we know that each "scroll" == 25 wines
    num_scrolls = math.ceil(num_wines/25)

    # while number of scrolls is greater than 0, keep scrolling to the end of the page, wait 15 seconds to give time to load, then continue to the next page
    while num_scrolls > 0 : 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(15)
        num_scrolls -= 1

    # get links for all the wines -- ignoring the following terms so that we only get the specific urls for the wines and not the regions, countries, or social media
    wines = driver.find_elements_by_css_selector("a.anchor__anchor--2QZvA")
    ignore = ['wine-countries', 'wine-regions', 'instagram', 'facebook', 'twitter', 'redirect']
    wine_links = [wine.get_attribute('href') for wine in wines if not any(ig in wine.get_attribute('href') for ig in ignore)]

    return wine_links

all_wine = get_wine_links(driver)

# once done with collecting links - pickle them so we don't have to run the scraping again
 with open('outfile', 'wb') as wine_pickle:
        pickle.dump(all_wine, wine_pickle)

# with open ('outfile', 'rb') as wine_pickle:
#     links = pickle.load(wine_pickle)
# driver.close()

# driver.quit()