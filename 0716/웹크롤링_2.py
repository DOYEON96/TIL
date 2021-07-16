# 벅스 뮤직 실시간 차트 데이터 가져오기
# - 웹 크롤링 기본적인 방법으로 데이터 연결(requests)

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import sys

url = 'https://music.bugs.co.kr/chart/track/day/total'
bugs_html = requests.get(url)

if bugs_html.status_code != 200:
    sys.exit('웹페이지 정보를 가져올 수 없습니다.')

bugs_soup = bs(bugs_html.text, 'lxml')
bugs_soup = bugs_soup.find('tbody')
tr_soup = bugs_soup.find_all('tr')

# print(tr_soup)
# 순위 곡명 아티스트 앨범

bugs_lst=[]
for tr in tr_soup:
    rank = tr.find('strong').get_text()
    title = tr.find('p', class_='title').get_text().replace('\n', '')
    artist = tr.find('p', class_='artist').get_text().replace('\n', '')
    album = tr.find('a', class_='album').get_text().replace('\n', '')
    bugs_lst.append({'순위':rank, '곡명':title, '아티스트':artist, '앨범':album})

df1 = pd.DataFrame(bugs_lst, columns=['순위', '앨범', '곡명', '아티스트'])
print(df1)
    