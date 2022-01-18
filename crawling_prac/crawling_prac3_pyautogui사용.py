import requests
from bs4 import BeautifulSoup
import pyautogui

search_word = pyautogui.prompt("검색어를 입력하세요.")
last_page = pyautogui.prompt("마지막 페이지번호를 입력해 주세요.")
page_num = 1
for i in range(1, int(last_page)*10, 10):
    print(f"{page_num}페이지 입니다. ========================================================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_word}&start={i}")
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".news_tit")
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    page_num += 1