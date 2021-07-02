import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

# df1 = pd.read_csv("./multi/0702/data/성적표.csv", encoding='cp949')

# # Series를 생성하는 방법 
# df1 = pd.Series( ['김도연', '김봉진'], name='이름')
# df3 = pd.Series( [26, 21], name='나이')
# print(df1)
# print(df3)
# # df0 = pd.concat([df1, df3], axis=1) # 시리즈 상태의 데이터들을 데이터프레임으로 함치는 방법
# print(df0)
# print(type(df0))
# # # DataFrame을 생성하는 방법 (딕셔너리 이용)
# df2 = pd.DataFrame( {
#     '이름' : ['aaa', 'bbb', 'ccc'],
#     '나이' : [25, 26, 21],
#     '성별' : ['남자', '남자', '여자']
# })
# print(df2)
# # dataframe 생성 두번째 방법 (리스트 이용)
# df1 = pd.DataFrame([['aaa', 25, 'male'], ['bbb', 26, 'male'], ['ccc', 21, 'female']], columns=['name', 'age', 'sex'])
# print(df1)

# # dataframe 생성 세 번째 방법 (딕셔너리 구조가 여러번)
# df1 = pd.DataFrame([{'name':'aaa', 'age':25, 'Sex':'male'},
#                     {'name':'bbb', 'age':26, 'Sex':'male'},
#                     {'name':'ccc', 'age':21, 'Sex':'female'}
#                     ])
# print(df1)

#####################################################################################################
# Pandas에서 결측치 처리

df1 = pd.read_csv("./multi/0702/data/성적표.csv", encoding='cp949')

# print(df1)

# 46번째 행에 쓰레기값 주입

# nan값 확인
# print(df1.isnull().sum())

# NaN값 처리 : 모든 데이터 NaN인 데이터 행 삭제
# dropna() 옵션 : default값은, how='any' - nan이 있는 모든 행 삭제, how='all' 행의 모든 칼럼값이 nan인 경우 삭제

# print(df1.dropna(how='all')) # 행 값이 전부 nan인 경우 삭제
# print(df1.dropna(how='all', axis=1)) # 열 값이 전부 nan인 경우 삭제

# print(df1.dropna(thresh=3)) # thresh = 결측치의 갯수, 결측치의 갯수가 지정 숫자 이상인 행 전체 삭제

# print(df1.dropna(thresh=3, inplace=True))
# print("dkd")
# df1=df1.dropna(thresh=3)
# print(df1)

##################################################
# pandas 모듈을 이용한 데이터 편집 및 관리
# - 이론, 실기 점수를 60~100 사이의 값으로 무작위 입력

df1['이론'] = random.randint(60,101, size=len(df1))
df1['실기'] = random.randint(60,101, size=len(df1))
print(df1.head(3))
print(df1.tail(3))

