import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import sys
from tqdm import tqdm

def news_parser(keyword, spage=1, epage = 1):
    news_list=[]
    for i in range(int(spage), int(epage) + 1):
        
        url = 'https://news.joins.com/Search/JoongangNews?page=' + str(i) # 페이지 번호
        url = url + '&Keyword=' + quote(keyword) + '&SortType=New&SearchCategoryType=JoongangNews' # 키워드
    

        res = requests.get(url)
        res.raise_for_status()
        soup = bs(res.text, 'lxml')

    
        li_soup = soup.find('ul', class_='list_default')
        li_text = li_soup.find_all('li')
    
        for li in li_text:

            title = li.find('h2').get_text()
            a_url = li.find('a')['href']
            day = li.find('span', class_='byline').find_all('em')[-1].get_text()
            body = body_text(url)
            news_list.append([title, day, body])

    df1 = pd.DataFrame(news_list, columns=['제목', '날짜', '내용'])

    return df1

def body_text(url):
    html = urlopen(url)
    soup = bs(html, 'lxml')

    try:
        body=soup.find('div', id='article_body').get_text()
    except:
        body = ''
    
    body = re.sub('[^0-9ㄱ-ㅣ가-힣]','', body)

    return body



if __name__ == '__main__':
    keyword = input('조회 키워드 입력 : ')
    spage = input('시작 페이지 번호 : ')
    epage = input('종료 페이지 번호 : ')

    df1 = news_parser(keyword, spage, epage)
    df1.to_csv('./multi/0721/data/중앙일보_'+keyword+'.csv', index = False, encoding='cp949')

    print('작업종료')