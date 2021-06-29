# csv 형식의 파일 읽어오기
# - csv 모듈 이용, open("파일 경로 및 파일명"), 오픈형식, encoding="cp949")
# - 오픈형식 : r = 읽기전용, w=파일생성 및 쓰기, a = 기존파일에 추가
# encoding > cp949 : 마이크로소프트에서 한글처리 방법(아스키코드), utf-8 범용(유니코드)
# pandas 모듈이용

# import os

# print(os.getcwd())

# csv 모듈 이용
# pandas 모듈 이용
copy=[]
import csv
import numpy as np
f=open("./multi/0629/data/seoul.csv", 'r', encoding='cp949')
data = csv.reader(f, delimiter = ',')

header=next(data)

for row in data:
    if row[2] and row[4] in "":
        continue
    else:
        copy.append(row)

f.close()

# copy[2] # 일시
# copy[4] # 최고기온
highdate = ""
hightemp = 0
for i in copy:
    if hightemp < float(i[4]):
        hightemp = float(i[4])
        highdate = i[2]
print(f"가장 온도가 높았던 날짜는 {highdate}이고, 그날의 온도는 {hightemp}입니다.")


########################################################

# pandas 모듈을 이용한 csv 파일 관리

# import pandas as pd

# df = pd.read_csv('./multi/0629/data/seoul.csv', encoding="cp949")
# print(df)

# print(df['최고기온(℃)'].max())

# print(df[df['최고기온(℃)']==df['최고기온(℃)'].max()])

# df.info()

#############################################################

