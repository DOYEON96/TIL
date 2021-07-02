import pandas as pd
from numpy import random
import matplotlib.pyplot as plt

# 미션
# - 남/여 칼럼에서 남자는 1 여자는 2로 각각 변경
# - 열 이름 > 성별코드
# - 열 순서 : 순번, 이름, 성별, 성별코드, 학과, 학년 이론, 실기

df1 = pd.read_csv("./multi/0702/data/성적표.csv", encoding='cp949')

# sexcode = []

df1['성별코드'] = [1 if xy == '남자' else 2 for xy in df1['남/여']]

# for i in df1['남/여']:
#     if i == '남자':
#         sexcode.append(1)
#     if i == '여자':
#         sexcode.append(2)
# print(sexcode)

df1['이론'] = random.randint(60,101, size = len(df1))
df1['실기'] = random.randint(60,101, size = len(df1))


# df1['성별코드']=sexcode
df1 = df1[['순번', '이름', '남/여', '성별코드', '학과', '학년', '이론', '실기']]
# print(df1)

df1['합계'] = df1['이론'] + df1['실기']
df1['평균'] = df1['합계']/2
# print(df1)

# pandas.dataframe 저장
# - csv : Dataframe.to_csv(경로/파일명.csv, index = True or False)
# - txt : Dataframe.to_csv(경로/파일명.txt, sep=",", index = True or False)
# - excel : Dataframe.to_excel(경로/파일명.xlsx, index = True or False, sheet_name ='시트명') / openpyxl 모듈 설치 필요
# - html : Dataframe.to_html('경로/파일명.html')

# df1.to_csv("multi/0702/data/성적1.csv")
# df1.to_csv("multi/0702/data/성적2.txt", sep='\t', index=False)
# df1.to_excel('multi/0702/data/성적3.xlsx', header=False)
# df1.to_html('multi/0702/data/성적4.html', index=False)

############################################################################
# pandas dataframe에서 인덱싱 하는 방법

# - Dataframe.loc[index,'열이름']
# - dataframe.loc[[index1,index2], ['열이름1', '열이름2']]

# - dataframe.iloc[행위치,열위치]
# - dataframe.iloc[행시작위치:행종료위치, 열시작위치:열종료위치]

# 방법
#       dataframe.loc[index] > 행 전체 출력
#       daframe.loc[index시작값:index종료값] 시작 ~ 종료값 다중행 출력
#       daframe.loc[index시작값:index종료값, ['열이름', '열이름']] 시작 ~ 종료값 다중행 원하는 열만 출력

# 방법
# column과 index는 무시한다.
# - dataframe.iloc[행위치,열위치]
# - dataframe.iloc[행시작위치:행종료위치, 열시작위치:열종료위치]

# Datafrane.sort_values() / Dataframe.sort_index()

# dataframe의 값을 기준으로 정렬 : DataFrame.sort_values(by=['열이름'], ascending= True or False)
# print(df1.sort_values(by=['학년'], ascending = True))

# df1.sort_values(by=['평균'], ascending = False, inplace=True)
# print(f1)

# df1.sort_values(by=['학년', '평균'], ascending=[True, False], inplace = True)
# print(df1.loc[0:9])
# df1 = df1.sort_index()
# print(df1)
# print(df1.loc[0:9])

# print(df1.reset_index()) # df1 인덱스 값 유지 후 새로운 인덱스 값 설정
df1.reset_index(drop=True) # df1 인덱스값 재설정 및 새로운 인덱스 값 설정

# dataFrame 행/열 삭제
# - DataFrame.drop(index = 0, axis = 0) # 1개의 행 삭제, index 값이 0인 데이터 행 삭제
# - DataFrame.drop(index=[0,1,2], axis=0) # 여러개의 행 삭제, index값이 0,1,2인 데이터 삭제
# - DataFrame.drop(df.loc[df['열이름']=='Yes'].index, inplace=True) # 
# - DataFrame.drop(DataFrame['열이름1', '열이름2'], axis=1) 정의한 열을 삭제

# df1.drop(0, inplace= True) # 0번째 행 삭제
# df1.drop([df1['평균'] < 90], inplace=True) # 0,2,4,6번 데이터 행 삭제
# df1.drop(df1.loc[df1['평균'] < 90].index, inplace=True) # 평균이 90 미만인 데이터 삭제
# print(df1)

df1.drop(['순번', '성별코드'], axis = 1, inplace=True)
print(df1)
# df1.drop(columns=['학과', '합계'], inplace=True)
# print(df1)

del df1['합계']
print(df1.head(3))