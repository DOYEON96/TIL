from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from tqdm import tqdm
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def url_parse():
    url = 'https://play.google.com/store/apps/details?id=com.coupang.mobile&showAllReviews=true'
    driver.get(url)
    driver.implicitly_wait(5)

    for i in range(1, 30):
        time.sleep(2)
        driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
        if (i % 5) == 0:
            
            driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span').click()
            
        time.sleep(1)
    
    txt = driver.find_elements_by_class_name('UD7Dzf')
    
    lst = []

    for j in range(1, len(txt) + 1):
        lst.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(j)+']/div/div[2]/div[2]/span[1]').text)
        
    return lst

## 


# main
driver = webdriver.Chrome('./chromedriver.exe')
lst = url_parse()
okt = Okt()

txt = ''
for i in lst:
    txt = txt + ' ' + i

f = open('./multi/0727/data/test.txt', 'w', encoding='utf-8')
f.write(txt)
f.close

### 쿠팡 긍/부정 
# 1. 구글 플레이스토어 쿠팡 이동
#     1. 셀리늄 사용
#     2. 5회 더보기 후 댓글 전체 가져오기
# 2. 댓글 전체 가져오기
# 3. 댓글을 이용한 긍정/부정 분석
#     1. TextBlob을 이용한 학습 후 긍/부정 분석(긍/부정 건수 비교) 시각화
#     2. 긍/부정 사전을 이용한 데이터 분석
#         1. konlpy를 이용해 단어구분(명사/형용사/동사/부사) # noun, adjective, verb, adverb
#         2. 불필요한 데이터 불용어 삭제
#         3. 토픽 분석 : 긍/부정 단어 개수 각각
#         4. 시각화 : 워드클라우드, 상위 단어의 빈도수를 이용한 시각화

f = open('./multi/0727/data/test.txt', 'r', encoding='utf-8')
txt = f.read()
f.close

okt = Okt()

pos = okt.pos(txt)

cnt = Counter(pos)

pos_txt=okt.pos(txt)

adjective=[okt[0] for okt in pos_txt if okt[1]=='Adjective']
noun=[okt[0] for okt in pos_txt if okt[1]=='Noun']
verb=[okt[0] for okt in pos_txt if okt[1]=='Verb']
adverb=[okt[0] for okt in pos_txt if okt[1]=='Adverb']

morph = adjective + noun + verb + adverb


stop_word = '로 것 제데ㅐ로 로 ( 것 크 ^ . ..'
stop_word = stop_word.split(' ')

SentiWord = pd.read_csv('c:/pythonworkspace/multi/0727/data/SentiWord_info.csv')
def pos_neg(word):
    tmp = SentiWord[(SentiWord['word']==word) | (SentiWord['word_root']==word)]
    try:
        word_res = (word, tmp['polarity'][tmp.index[0]])
    except:
        word_res = (word, 0)
    return word_res

pos_lst=[]
neg_lst=[]
unknown_lst=[]

for noun in tqdm(morph):
    word_res = pos_neg(noun)
    if word_res[1] > 0:
        pos_lst.append(word_res[0])
    elif word_res[1] < 0:
        neg_lst.append(word_res[0])
    else:
        unknown_lst.append(word_res[0])

pos_lst = [sw for sw in pos_lst if sw not in stop_word]
neg_lst = [sw for sw in neg_lst if sw not in stop_word]
unknown_lst = [sw for sw in unknown_lst if sw not in stop_word]


print(f'긍정 단어의 수 : {len(pos_lst)}')
print(f'부정 단어의 수 : {len(neg_lst)}')

txt_cnt = Counter(morph)

most_lst = txt_cnt.most_common()

most_df=pd.DataFrame(most_lst, columns=['토픽', '빈도']) 
most_df = most_df[:16] # 상위 15개만 차트 이용

plt.figure(figsize=(15, 8))
plt.subplot(2, 2, 1)
plt.plot(most_df['토픽'], most_df['빈도'])

plt.subplot(2, 2, 2)
plt.pie(most_df['빈도'], labels = most_df['토픽'], autopct='%.1f%%')

plt.subplot(2, 2, 3)
plt.bar(most_df['토픽'], most_df['빈도'])

most_df=pd.DataFrame(most_lst, columns=['토픽', '빈도']) 
most_df = most_df[:16] # 상위 15개만 차트 이용

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=50, max_font_size=300)

wc = wordcloud.generate_from_frequencies(txt_cnt)
plt.subplot(2, 2, 4)
plt.imshow(wc)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")

plt.show()