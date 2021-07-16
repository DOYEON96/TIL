# 멜론 차트 정보 가져오기
# - selenium 모듈 사용
# - selenium 모듈은 chromedriver.exe를 사용해 크롬 브라우저를 직접 컨트롤
# - 크롬 드라이버 설치

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

driver=webdriver.Chrome('./chromedriver.exe')
# time.sleep(5) # 5초 대기

url = 'https://www.naver.com/'
driver.get(url)

tr_soup = melon_soup.find_all('tr')

melon_list=[]
cnt = 0

for tr in tr_soup:
    cnt +=1
    rank = cnt
    title = tr.find('div', class_='ellipsis rank01').get_text().replace('\n', '')
    artist = tr.find('div', class_='ellipsis rank01').get_text().replace('\n', '')
    title = tr.find('div', class_='ellipsis rank01').get_text().replace('\n', '')
    title = tr.find('div', class_='ellipsis rank01').get_text().replace('\n', '')
    