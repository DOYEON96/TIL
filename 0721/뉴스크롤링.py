# requests vs urllib.request
# - 데이터를 보낼 때 requests는 딕셔너리 형태, urllib은 인코딩하여 바이너리 형태로 전송
# - requests는 요청 메소드(get, post)를 명시하지만 urllib은 데이터의 여부에 따라 get과 post 요청을 구분
# - 없는 페이지 요청시 requests는 코드값을 반환하지만 urllib은 에러를 띄운다

import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

def url_parser(keyword, spage=1, epage = 1):
    
    url = 'https://news.joins.com/Search/JoongangNews?page=' + str(page) # 페이지 번호
    url = url + '&Keyword=' + quote(keyword) + '&SortType=New&SearchCategoryType=JoongangNews' # 키워드
    
    # return url

    res = requests.get(url)
    res.raise_for_status()
    soup = bs(res.text, 'lxml')

    # return soup

    # soup = url_parser('올림픽', 1)
    #1. li_soup = soup.select('div.bd > ul.list_default > li')
    li_soup = soup.find('ul', class_='list_default')
    li_text = li_soup.find_all('li')

    news_list=[]
    for li in li_text:

        title = li.find('h2').get_text()
        a_url = li.find('a')['href']
        body = li.find('span', class_='lead').text
        day = li.find('span', class_='byline').find_all('em')[-1].text

        news_list.append([title, a_url, body, day])

        df1 = pd.DataFrame(news_list, columns=['제목', 'url', '내용', '날짜'])

    return df1
    

df1 = url_parser('올림픽', 2)

# html = urlopen(df1['url'][0])
# soup = bs(html, 'lxml')
# print(soup)

title_list=[]
body_list=[]

for df_url in df1['url']:
    html = urlopen(df_url)
    soup = bs(html, 'lxml')

    title = soup.find('h1', class_='headline mg').get_text()
    try:
        body = soup.find('div', id='article_body').get_text()
    except:
        body=""


    title_list.append(re.sub('[^0-9ㄱ-ㅣ가-힣]',"", title)) # 숫자/한글/영문 모두 ""로 변경
    body_list.append(re.sub('[^0-9ㄱ-ㅣ가-힣]',"", body))

df2=pd.DataFrame({'제목':title_list, '상세내용':body_list})
print(df2)

###############################################
# 문자열 정규화

# txt = '''
# 안녕하세요.~~~~
# 반갑습니다.ㅋㅋㅋㅋ
# body, html, H1, 1234
# '''

# print(re.sub('[a-zㄱ-ㅣ0-9]', '', txt))
# print(re.sub('[^a-zㄱ-ㅣ0-9]', '', txt)) # ^를 포함하면 포함된 문자열만 남기고 ""로 변경

##############################################
# print(df1)