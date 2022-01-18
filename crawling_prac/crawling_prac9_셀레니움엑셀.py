from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get('https://www.naver.com')

browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

before_h = browser.execute_script('return window.scrollY')

while True:
    browser.find_element_by_css_selector('body').send_keys(Keys.END)
    time.sleep(1)
    after_h = browser.execute_script('return window.scrollY')
    if after_h == before_h:
        break
    before_h = after_h

file = open(r'C:\Users\ahnhy\OneDrive\바탕 화면\2022\NAMZ\Python_prac\crawling_prac\data.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(file)

items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    price = item.find_element_by_css_selector(".price_num__2WUXn").text
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    print(name, price, link)
    csvWriter.writerow([name, price, link])

file.close()