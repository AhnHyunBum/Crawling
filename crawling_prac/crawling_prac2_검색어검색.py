import requests
from bs4 import BeautifulSoup
import pyautogui

search_word = pyautogui.prompt("검색어를 입력하세요.")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")
for link in links[:5]:
    title = link.text
    url = link.attrs['href']
    print(title, url)