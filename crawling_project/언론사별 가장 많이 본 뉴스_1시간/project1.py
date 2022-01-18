from lib2to3.pgen2 import driver
from selenium import webdriver
import csv

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100')

file = open(r'C:\Users\ahnhy\OneDrive\바탕 화면\2022\NAMZ\Python_prac\crawling_project\언론사별 가장 많이 본 뉴스_1시간\data.csv', 'w', encoding='CP949', newline='')
csvWriter = csv.writer(file)

time = browser.find_element_by_css_selector('.section_sub_txt').text

article = []
btn = browser.find_element_by_css_selector("button.refresh_button")

items = browser.find_elements_by_css_selector('.list_text_inner')
for item in items:
    name = item.find_element_by_css_selector(".list_text_inner > a").text
    if name != '':
        if name not in article:
            article += [name]
    else:
        btn.click()
        
csvWriter.writerow([time])
for a in article:
    csvWriter.writerow([a])
csvWriter.writerow([])
        

