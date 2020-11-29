# imports
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from htmldom import htmldom
from bs4 import BeautifulSoup
driver = webdriver.Chrome('/Users/pawelzielinski00/Desktop/chromedriver')
driver.get('https://www.linkedin.com/login/pl?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('password')
username.send_keys('M@jonez6666')
sleep(0.5)

password = driver.find_element_by_id('username')
password.send_keys('zpawlo02@gmail.com')
sleep(0.5)

sign_in_button = driver.find_elements_by_class_name('btn__primary--large')
sign_in_button[0].click()

driver.get('https://www.linkedin.com/search/results/all/?keywords=programista%20polska&origin=GLOBAL_SEARCH_HEADER')
sleep(3.5)

elems = driver.find_elements_by_css_selector(".search-results-container [href]")
links = [elem.get_attribute('href') for elem in elems]
se = set(links)
for link in se:
    if(link[25] == 'i'):
        print(link)


