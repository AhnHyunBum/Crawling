from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get('https://www.naver.com')

browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)