## 한글 형태소 분석
# konlpy : https://konlpy.org/ko/v0.5.2/


from konlpy.tag import Okt
from nltk import Text
from wordcloud import WordCloud
import matplotlib.pyplot as plt




f=open('./multi/0722/data/2021_신년사.txt', 'r')
txt = f.read()

f.close()

t = Okt()
# print(t.tagset) # Okt 모듈의 tag 세팅 출력

pos_txt = t.pos(txt) # txt의 토픽(단어)들 품사단위 표현
# print(pos_txt)

nouns_txt = t.nouns(txt)    # 토픽(단어)들 중
# print(nouns_txt)

# 원하는 품사별 리스트 정리
#1 
## txt 파일에서 형용사만 추출

# Adjective = [t[0] for t in pos_txt if t[1] =='Adjective']
## 명사만 추출
# Noun = [t[0] for t in pos_txt if t[1] =='Noun']
## 동사만 추출
# Verb = [t[0] for t in pos_txt if t[1] =='Verb']

# print(f'[형용사]\n{Adjective}')
# print(f'[명사]\n{Noun}')
# print(f'[동사]\n{Verb}')

# 2 
Adjective = []
Noun = []
Verb = []
for t in pos_txt:
    if t[1] == 'Adjective':
        Adjective.append(t[0])
    elif t[1] == 'Noun':
        Noun.append(t[0])
    elif t[1] == 'Verb':
        Verb.append(t[0])

# print(Adjective)
# print(Noun)
# print(Verb)

morph = Adjective + Noun + Verb

from collections import Counter # jdk에서 제공하는 기본 라이브러리

morph_cnt = Counter(morph) # morph 리스트의 형태소별 카운트값을 저장
# print(morph_cnt)

morph_txt = morph_cnt.most_common() # 딕셔너리 구조의 데이터를 내림차순 정렬 후 튜플 구조로 변경
# print(f'[전 체]\n{morph_txt}')

# morph_txt 에서 5회이상 거론된 토픽만 추출
morph_mod = []
for i in morph_txt: # keyword와 num에 각각 형태소와 카운트값 저장
    if i[1] >= 5:
        morph_mod.append(i)

# print(morph_txt)

morph_txt = dict(morph_txt)
# print(morph_txt)

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=100, max_font_size=300)

wc = wordcloud.generate_from_frequencies(morph_txt)
plt.figure(figsize=(8,15))
plt.imshow(wc)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
