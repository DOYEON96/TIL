from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import Text
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

f = open('./multi/0723/data/제주도맛집_질문.txt', 'r')
title_txt = f.read()
f.close

okt = Okt()
pos_title = okt.pos(title_txt)

noun = [txt[0] for txt in pos_title if txt[1] == 'Noun']
adjective = [txt[0] for txt in pos_title if txt[1] == 'Adjective']
# print(Counter(noun))

most_txt = noun + adjective

stop_word = '제주도 맛집 부탁드립니다'
stop_word = stop_word.split(' ')

most_txt = [sw for sw in most_txt if sw not in stop_word]
most_cnt = Counter(most_txt)
# print(most_cnt)

most_lst = most_cnt.most_common()
most_df=pd.DataFrame(most_lst, columns=['토픽', '빈도'])
print(most_df[most_df['빈도']>=3])


most_cnt = dict(most_cnt)

wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      background_color="white", width=1000, height=1000,
                      max_words=100, max_font_size=300)

wc = wordcloud.generate_from_frequencies(most_cnt)
plt.figure(figsize=(8,15))
plt.imshow(wc)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
# plt.show()

most_df.plot()
most_df.set_index = most_df['빈도']
most_df.plot.bar(figsize=(14,5))
plt.show()