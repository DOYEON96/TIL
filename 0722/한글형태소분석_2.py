from konlpy.tag import Okt
from nltk import Text
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import nltk


f=open('./multi/0722/data/2021_신년사.txt', 'r')
texts = f.read()

f.close()

t=Okt()
pos_txt=t.pos(texts)

형용사=[t[0] for t in pos_txt if t[1]=='Adjective']
명사=[t[0] for t in pos_txt if t[1]=='Noun']
동사=[t[0] for t in pos_txt if t[1]=='Verb']

morph = 명사+형용사+동사
morph = Text(morph) # nltk 라이브러리 모듈

plt.plot(morph)

morph.dispersion_plot(['국민', '것', '경제', '코로나'])

# stopword(불용어) 만들기
# stop_word=['.', ',','(', ')',"'", '입니다', '있습니다', '하겠습니다', '여러분', '수', '할', '해', '위', '델', '등', '감사합니다', '되었습니다', '합니다']

# 불용어 처리 #2
stop_word = '. , 입니다 있습니다 여러분 수 할 해 위 델\
등 감사합니다 되었습니다 하겠습니다 합니다'

morph_stop = [sw for sw in morph if sw not in stop_word]
# print(morph_stop)

stop_word = stopword.split(' ')


morph_cnt = Counter(morph_stop)
morph_txt = morph_cnt.most_common()

morph_txt_up = [t for t in morph_txt if t[1] >= 5 ]
# morph_txt_up.remove(('입니다', 47))
# print(morph_txt_up)

morph_txt_up = dict(morph_txt_up)

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=100, max_font_size=300)

wc = wordcloud.generate_from_frequencies(morph_txt_up)
plt.figure(figsize=(8,15))
plt.imshow(wc)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()



