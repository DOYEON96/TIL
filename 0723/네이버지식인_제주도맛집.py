## 네이버 API를 이용해 원하는 정보 수집(지식인)
## 세부 내용(질문/답변)
## 질문에 대한 토픽분석/답변에 대한 토픽분석
## - 빈도수/워드클라우드/차트/연관 관계
# requests 모듈을 이용한 방법

import sys
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from nltk import Text
import pandas as pd
import re
from urllib.parse import quote
import json


def api_parse(encText, sPage=1):
    url = "https://openapi.naver.com/v1/search/kin?query=" + encText # json 결과
    url = url + '&start=' + str(sPage) + '&display=100'

    request = requests.get(url)

    headers={'X-Naver-Client-Id':'',
    'X-Naver-Client-Secret':''}

    res_json = requests.get(url, headers=headers)
    

    if(res_json.status_code==200):
        res_body = res_json.json()
    else:
        print("Error Code:" + res_json.status_code)
        sys.exit(0)

    # print(res_body)
    # print(res_body['items'][0]['link']) # 첫번째 아이템의 링크 값 출력

    res_df = pd.DataFrame(res_body['items'])

    return res_df
# print(res_df)

# 세부 정보 가져오기
# - res_df의 link 정보를 이용해 세부 내용 가져오기
# - 질문 정보 : keyword_질문.txt 파일로 저장
# - 답변 정보 : keyword.답변.txt 파일로 저장

## 전역변수
client_id = ''
client_secret = ''

title_lst=[]
answer_lst=[]


## 메인

# encText = quote(input("검색할 단어 입력 : ")) # 바이너리값으로 변경
# sPage=input('시작 페이지 : ')

encText = '제주도맛집'
sPage = 1

df1 = api_parse(encText, sPage)

fq = open('./multi/0723/data/'+encText+'_질문.txt', 'w')
fa = open('./multi/0723/data/'+encText+'_답변.txt', 'w')

link_lst = list(df1['link'])

for link in link_lst:
    kin_html = requests.get(link)
    kin_html.raise_for_status()
    kin_soup = bs(kin_html.text, 'lxml')
    try:
        kin_txt = kin_soup.find('div', class_='title').get_text() # 질문정보
        kin_txt = kin_txt.replace('\n','').replace('\t','')
        fq.write(kin_txt+'\n')
    except:
        print(link)
        fq.write('\n')

    

    # print(kin_txt + '')
    for txt in kin_soup.find_all('div', class_="se-component se-text se-l-default"): # 답변 정보
        fa.write(re.sub('[^ㄱ-ㅣ가-힣0-9]','', txt.text))
        # print(txt.text.replace('\u200b',''))
    fa.write('\n')
    
fq.close()
fa.close()
