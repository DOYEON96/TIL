# 사용자들로부터 구 이름, 동 이름 입력받아서 데이터 조회
# 출력값 : '자치구명', '법정동명', '건물주용도', '건축 년도', '건물면적', '층 정보', '물건금액', '건물명'
# 출력형식 : 리스트 구조 출력

# 구 별 동단위 건물 주용도 별 평균 시세

import csv
import matplotlib.pyplot as plt

f = open('./multi/0701/data/서울특별시_부동산_실거래가_정보_2020년.csv')
data = csv.reader(f)
header=next(data)

G_name=input("조회할 구 이름을 입력해주세요 : ")
# D_name=input("조회할 동 이름을 입력해주세요 : ")
data_lst=[]
for row in data:
    if G_name in row[3]: # row[3] 구 이름 row[5] 동 이름
        data_lst.append([ row[3], row[5], row[15], row[17], row[11], row[13], row[16], row[18] ])
f.close()
# print(data_lst)


# 동 별 아파트 평균 가격 계산
## 해당 구에 어떤 동이 있는지 동 리스트 찾기
## 해당 리스트를 이용해 동 별 아파트 평균계산
## 동별 평균 출력

# 동별 평균 계산값을 그래프를 이용해 비교분석
## 막대그래프
## 상자그림

############################################################333

d_name=[]
price=[]
avg_lst=[]

for lst in data_lst:
    if lst[1] in d_name:
        continue
    else:
        d_name.append(lst[1])

for dong in d_name:
    tot=0
    cnt=0

    for lst in data_lst:
        if dong == lst[1] and '아파트' == lst[2]:
            tot += int(lst[-2])
            cnt += 1
    if cnt == 0:
        avg_lst.append({"동이름":dong, "평균판매가":0, "거래건수":cnt})
    else:
        avg = tot / cnt
        avg_lst.append({"동이름":dong, "평균판매가":avg, "거래건수":cnt})

# print(avg_lst)

#################################################################

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


df = pd.DataFrame(avg_lst)
# print(df)



df1 = df[df['평균판매가']!=0]
df1.sort_values(by='평균판매가', ascending=False, inplace=True) # ascending=False 내림차순, inplace 정렬 데이터를 변수에 바로 적용
# 위아래 같음
# df1 = df1.sort_values(by='평균판매가', ascending=False)

df1=df1.sort_index()
print(df1)

# df1['평균판매가'].plot()
# plt.figure(figsize=(15, 5))
# plt.xticks(size=10, rotation=45)
# plt.plot(df1['동이름'], df1['거래건수'])
# plt.show()

## barplot으로 출력
# plt.style.use('ggplot')
# plt.figure(figsize=(15, 5))
# plt.xticks(size=10, rotation=45)
# plt.bar(df1['동이름'], df1['평균판매가'])

# plt.title(G_name + ' 동별 아파트 평균 판매가 분석')
# plt.show()

## boxplot 
### 연속형 변수에 대해서 최소값 1사분위수 중앙값 3사분위수 최대값 등의 요약 통계량을 보기 위해 사용

plt.style.use('ggplot')
plt.figure(figsize=(15, 5))
plt.xticks(size=10, rotation=45)
plt.boxplot(df1['평균판매가'])
plt.show()