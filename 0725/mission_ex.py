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
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import matplotlib.font_manager as fm
import time
import pyperclip
from konlpy.tag import Okt, Kkma, Hannanum

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def naver_parse(keyword):
    item_lst=[]
    for page in range(1, 2):
        url = 'https://openapi.naver.com/v1/search/kin?query=' + quote(keyword)
        url = url + '&display=100' + '&start=' + str(page)

        headers={'X-Naver-Client-Id':'',
        'X-Naver-Client-Secret':''}

        res = requests.get(url, headers=headers)
        res.raise_for_status
        # res_soup = bs(res.text, 'lxml')
        res_json = res.json()
        res_items = res_json['items']
        
        for i in res_items:
            item_lst.append(i['link'])


    return item_lst

def link_parse(lst):

    for link in tqdm(lst):
        kin_html = requests.get(link)
        kin_html.raise_for_status()
        kin_soup = bs(kin_html.text, 'lxml')
        try:
            kin_txt = kin_soup.find('div', class_='title').get_text() # 질문정보
            kin_txt = kin_txt.replace('\n','').replace('\t','')
            fq.write(kin_txt+'\n')

            for txt in kin_soup.find_all('div', class_="se-component se-text se-l-default"): # 답변 정보
                fa.write(re.sub('[^ㄱ-ㅣ가-힣0-9]+',' ', txt.text))
            
            fa.write('\n')

        except:
            selenium_parse(link)

    fq.close()
    fa.close()
    driver.close()

def selenium_parse(link):

    driver.get(link)
    driver.implicitly_wait(10)
    
    ans = driver.find_elements_by_class_name("se-main-container")
    
    kin_txt = driver.find_element_by_class_name('title').text
    kin_txt = kin_txt.replace('\n','').replace('\t','')
    fq.write(kin_txt+'\n')

    for txt in ans:
        
        fa.write(re.sub('[^ㄱ-ㅣ가-힣0-9]+',' ', txt.text))
        fa.write(' ')
    fa.write('\n')
    time.sleep(1)
    
    

def naver_login():

    print('로그인중입니다.')
    keys = Keys()

    driver.find_element_by_xpath('//*[@id="account"]/a').click()
    time.sleep(2)

    tag_id = driver.find_element_by_id('id') # 아이디 입력란 객체 정의
    tag_pw = driver.find_element_by_id('pw') # 비밀번호 입력란 객체 정의
    

    tag_id.clear()
    tag_id.click()
    time.sleep(1)
    pyperclip.copy('')
    tag_id.send_keys(keys.CONTROL, 'v')
    time.sleep(2)
    

    tag_pw.clear()
    tag_pw.click()
    time.sleep(1)
    pyperclip.copy('')
    tag_pw.send_keys(keys.CONTROL, 'v')
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    
def question_anal(keyword):

    fq = open('./multi/0723/data/'+keyword+'_질문.txt', 'r')
    ques = fq.read()
    fq.close

    pos = okt.pos(ques)

    noun = [txt[0] for txt in pos if txt[1] == 'Noun']
    adjective = [txt[0] for txt in pos if txt[1] == 'Adjective']

    most_txt = noun + adjective

    stop_word = '질문 요 수 이번 있나요 언제 왜 사람 내공 대한 에어팟 더 때문 댓글 현재 및 좀 정도 다음 어떻게 있을까요 하나요 이유 무엇 만날 번 달 가지 누가 뭔가'
    stop_word = stop_word.split(' ')

    most_txt = [sw for sw in most_txt if sw not in stop_word]

    most_cnt = Counter(most_txt)

    most_lst = most_cnt.most_common()

    most_df=pd.DataFrame(most_lst, columns=['토픽', '빈도'])
    most_df = most_df[most_df['빈도']>=15]

    print(most_df)

    most_cnt = dict(most_cnt)

    

    wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=50, max_font_size=300)

    wc = wordcloud.generate_from_frequencies(most_cnt)
    plt.figure(figsize=(8,15))
    plt.imshow(wc)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def answer_anal(keyword):

    fa = open('./multi/0723/data/'+keyword+'_답변.txt', 'r')
    ans = fa.read()
    fa.close

    # print(ans)

    pos = okt.pos(ans)
    # print(pos)

    noun = [txt[0] for txt in pos if txt[1] == 'Noun']
    adjective = [txt[0] for txt in pos if txt[1] == 'Adjective']

    most_txt = noun + adjective

    stop_word = '질문 요 수 이번 있나요 언제 왜 사람 내공 대한 에어팟 더 때문 댓글 현재 및 좀 정도 다음 어떻게 있을까요 하나요'
    stop_word = stop_word.split(' ')

    most_txt = [sw for sw in most_txt if sw not in stop_word]

    most_cnt = Counter(most_txt)

    most_lst = most_cnt.most_common()

    most_df=pd.DataFrame(most_lst, columns=['토픽', '빈도'])
    most_df = most_df[most_df['빈도']>=15]

    most_cnt = dict(most_cnt)

    wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=50, max_font_size=300)

    wc = wordcloud.generate_from_frequencies(most_cnt)
    plt.figure(figsize=(8,15))
    plt.imshow(wc)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()


## 전역변수

test=[]

chs = -1


## main

# driver = webdriver.Chrome('./chromedriver.exe')
# naver = 'https://www.naver.com/'
# driver.get(naver)

# naver_login()

keyword = input('검색할 키워드를 입력해주세요 : ')

# item_lst = naver_parse(keyword)
# fq = open('./multi/0723/data/'+keyword+'_질문.txt', 'w')
# fa = open('./multi/0723/data/'+keyword+'_답변.txt', 'w')
# link_parse(item_lst)

okt = Okt()
kkma = Kkma()
han = Hannanum()

# pos = han.pos(txt)
# print(pos)

chs = input('선택해주세요 : ')
if chs == str(1):
    question_anal(keyword)
elif chs == str(2):
    answer_anal(keyword)




# # print(Counter(noun))


# most_txt_ans = ans_noun + ans_adjective




# most_txt_ans = [sw for sw in most_txt_ans if sw not in stop_word]

# most_cnt_ans = Counter(most_txt_ans)

# print(most_cnt_ques)
# print(most_cnt_ans)


# print(most_lst_ques)
# most_lst_ans = most_cnt_ans.most_common()

# most_df.plot()
# most_df.set_index = most_df['빈도']
# most_df.plot.bar(figsize=(14,5))
# plt.show()