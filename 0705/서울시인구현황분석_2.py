import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


df1=pd.read_csv('./multi/0705/data/report.txt', sep ='\t', header=1)

df1 = df1.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]]

df1.drop(0, inplace = True)

col_name = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세이상']

df1.columns = col_name

df2 = df1.iloc[:, [0, 1, 2, 5, 8, 11]]

df2 = df2[df2['내국인'] != '…']

for i in range(2, len(df2.columns)):
    df2.iloc[:,i] = df2.iloc[:,i].str.replace(',','')

df2 = df2.astype({'총인구':'int64', '내국인':'int64', '외국인':'int64', '65세이상':'int64'})
# print(df2.dtypes)

gu = input("조회할 구 이름 입력 : ")
df3 = df2[df2['자치구'] == gu]

plt.figure(figsize=(10, 5))
plt.style.use('ggplot')
plt.xticks(size=10, rotation=45)

plt.plot(df3['년도'], df3['내국인'], marker='o', markersize=10, label='내국인')
plt.plot(df3['년도'], df3['외국인'], marker='o', markersize=10, label='외국인')
plt.plot(df3['년도'], df3['65세이상'], marker='o', markersize=10, label='65세이상')
plt.legend()
plt.title('서울 내/외국민 및 고령자 현황 분석 그래프(1992~2020)', size = 20)
plt.xlabel('년도')
plt.ylabel('인구수')

plt.show()