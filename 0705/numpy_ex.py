# 년도별 서울시 인구 현황(내국인, 외국인, 고령자)
# 년도별 외국인 남/여 비율
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

# 구분자가 \t인 경우
# 제목행 선택 : header = 행번호
df1 = pd.read_csv('./multi/0705/data/report.txt', sep='\t', header=1)

# 기간, 자치구, 전체, 전체 남성, 전체 여성, 내국인 전체, 내국인 남성, 내국인 여성, 외국인 전체, 외국인 남성, 외국인 여성, 65세 이상

df1 = df1[ ['기간', '자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1', '한국인.2', '등록외국인', '등록외국인.1', '등록외국인.2', '65세이상고령자'] ]
# df1.loc[:, ['기간', '자치구', '합계', '합계.1', '합계.2', '한국인', '한국인.1', '한국인.2', '등록외국인', '등록외국인.1', '등록외국인.2', '65세이상고령자']]
# df1.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]] # 다 같은 방법

df1 = df1.drop(0)

# 열이름 중 일부를 변경할 때
df1 = df1.rename(columns={'합계':'총인구', '한국인':'내국인', '등록외국인':'외국인'}) 
# print(df1.head())

# 열이름 전부 변경할 때
# df1.columns = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세이상']
# print(df1.head())

colname = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세이상']

df1.columns = colname
# print(df1.head())

# print(df1.info())

df2 = df1.iloc[:, 0:5]
# print(df2.head())





# df2['총인구'] = df2['총인구'].replace(",", "")

# df2['총인구'] = df2['총인구'].str.replace(',', '')
# df2['총인구(남)'] = df2['총인구(남)'].str.replace(',', '')
# df2['총인구(여)'] = df2['총인구(여)'].str.replace(',', '')

for i in range(2, len(df2.columns)):
    df2.iloc[:,i] = df2.iloc[:,i].str.replace(',','')

# pandas에서 데이터 타입 변경
# 모든 열 변경
# df2 = df2.astype(int64)

# 특정 열 데이터 타입 변경
df2 = df2.astype({'년도':int, '총인구':'int64', '총인구(남)':int, '총인구(여)':int})

# print(df2.dtypes)

gu = input('조회할 구 이름 입력해주세요 : ')

df3 = df2[df2['자치구'] == gu]

# plt.plot(df3['년도'], df3['총인구'], label='총인구')
# plt.plot(df3['년도'], df3['총인구(남)'], label='총인구(남)')
# plt.plot(df3['년도'], df3['총인구(여)'], label='총인구(여)')
# plt.title(gu+' 인구수 추이')
# plt.legend(loc='best')
# plt.show()

df3.plot(kind='hexbin', x='총인구', y='년도', gridsize = 20) # kind=hexbin > 산점도 그래프

df3.plot(kind='bar', x='년도', y=['총인구(남)', '총인구(여)']) # barplot에 두가지 데이터 비교
plt.show()

##########################################################################################

print(df1[df1['내국인'] != '…'])

