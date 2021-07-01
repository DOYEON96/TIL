# 구단위 동별 물건금액 평균값을 차트로 시각화
# - 구 이름, 건물주용도는 사용자에게 입력받아 진행
# - 출력 평균은 동을 기준으로 계산 및 출력

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df1=pd.read_csv('multi/0701/data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding='cp949')

G_name = input("검색을 원하는 자치구명을 입력하세요 : ")
purpose = input("검색을 원하는 건물주용도를 입력하세요 : ")

df1 = df1[(df1['자치구명']==G_name) & (df1['건물주용도']==purpose) ][['법정동명', '물건금액']]

df2 = df1.groupby('법정동명').mean()

df2.plot(kind='bar')
plt.show()