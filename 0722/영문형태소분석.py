from nltk.tokenize import RegexpTokenizer  # 정규표현식 문장에 적용
from nltk import Text
import matplotlib.pyplot as plt

# f = open('./multi/0722/data/test.txt', 'r')
# txt = f.read() # read() : 전체 데이터 읽기, readline() : 한줄단위 읽기, readlines() : 한줄단위 리스트형태로 전체저장
# # print(txt) 
# f.close()

# plt.rcParams["figure.figsize"]=(14, 5)
# retok=RegexpTokenizer("[\w]+")   # [a-zA-Z0-9_] 영문자(대소문자)와 숫자를 제외한 나머지 글자 제거
# txts=Text(retok.tokenize(txt))
# print(txts)

# plt.title('NLTK Test')
# txts.plot()               # 각 단어(토큰)의 사용 빈도를 그래프로 표현(Text 클래스에서 제공)
# plt.show()                # Text 클래스 : 문서 분석용 클래스, 토큰열 입력 생성

# txts.dispersion_plot(['you', 'for', 'set', 'free'])
# plt.show()

############################################

import nltk
nltk.download('book', quiet=True)
from nltk.book import *
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


emma_raw = nltk.corpus.gutenberg.raw("austen-emma.txt")
# print(emma_raw[:1302])
# print(emma_raw[:10])

# print(nltk.corpus.gutenberg.fileids())

## Text 클래스 : 문서 분석용 클래스, 토큰열 입력 생성
retok=RegexpTokenizer("[\w]+")
# print(Text(retok.tokenize((emma_raw[50:100]))))

text = emma_raw[50:100]
tag_list = pos_tag(word_tokenize(text))
# print(tag_list)
# print(word_tokenize(text))

nouns_list=[t[0] for t in tag_list if t[1]=='NNP' or t[1]=='NN']
print(nouns_list)