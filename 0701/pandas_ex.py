# 판다스 모듈 기본 구조
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df1 = pd.read_csv('./multi/0701/data/서울특별시_부동산_실거래가_정보_2020년.csv', encoding='cp949')
# print(df1.head())

# print(df1[df1['자치구명']=='서초구'].head())

# print(df1[['자치구명', '건물주용도']])



df1 = df1[['자치구명', '법정동명', '건물주용도', '건축년도', '건물면적', '층정보', '물건금액', '건물명']]
# print(df1)
# print(df1.columns)
# print(df1.info())

## 데이터프레임에서 결측값 처리하기
# print(df1.isnull().sum()) # 열 단위 NaN 값의 갯수 확인하기

# print(df1[df1['건축년도'].isnull()])
# print(df1[df1['층정보'].isnull()].head(3))
# print(df1[df1['층정보'].isnull()].tail(3))
df1 = df1.fillna({'층정보':1, "건물명":'단독','건축년도':0})


# nan 데이터 삭제 : dropna() 함수 사용, 파라미터 : how = any - nan이 하나라도 존재하면 삭제
#                                                how = all - 데이터 전체가 nan일 경우 삭제

# print(df1)
# print(df1.isnull().sum())

# pandas.dataFrame 데이터 관리
## 데이터 검색
# - 단일조건 : df[ df['열이름']==조건]
# - 다중조건 : df[ (df['열이름']==조건1) & (df['열이름']==조건2) ] & and 연산
# - 다중조건 : df[ (df['열이름']==조건1) | (df['열이름']==조건2) ] | or 연산

# print(df1['자치구명'].unique())

# print(df1[df1['자치구명']=='성북구'])
# print(df1[df1['자치구명']=='성북구']['법정동명'].value_counts()) # 자치구별 동을 찾고 각각 몇회 인지 카운트

df2 = df1[ (df1['자치구명']=='서초구') & (df1['건물주용도'] == '아파트') ]['법정동명'].value_counts() # 카운트가 0인 경우 출력하지 않음

print(df2)

df2.plot(kind='barh', figsize=(10, 3))
plt.show()

df3 = df1[ (df1['자치구명']=='서초구') & (df1['건물주용도'] == '아파트') ]
print(df3.groupby('법정동명').mean())

plt.plot(kind='pie')