import 기상청날씨정보 as wt
import 서울시지하철승하차현황_API as sw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

# sDt = input('시작일을 입력해주세요 : ')
# eDt = input('종료일을 입력해주세요 : ')

# df1 = wt.main()
# df2 = sw.main_api(sDt), eDt)

df1 = pd.read_csv('./multi/0715/data/서울_일별기상정보_20210101_20210714.csv', encoding='cp949')
df2 = pd.read_csv('./multi/0715/data/seoul_sw_inout.csv')

# df1 : 날짜, df2: 사용일 날짜형 데이터로 변경
# df1 : 평균기온, 최저기온, 최고긴온, 일강수량 > 실수형
# df2 : 승차/하차 > 정수형

# print(df1.head())

df1['날짜'] = pd.to_datetime(df1['날짜'], format = '%Y-%m-%d')

df2['사용일'] = pd.to_datetime(df2['사용일'], format = '%Y%m%d')
df2 = df2.rename(columns={'사용일':'날짜'})

df1 = df1.astype( {'평균기온':float, '최저기온':float, '최고기온':float, '일강수량':float} )
df2 = df2.astype( {'승차':int, '하차':int} )

# print(df1.info())
# print(df2.info())



# 조회역 이름과 날짜 입력시 해당 날짜의 역 탑승인원 차트 출력
# - 시계열 차트(강수량/승차인원)
# - 산점도

scLine = input("조회할 역 입력 : ")

df2[df2['역명']==scLine]



df3 = df2[df2['역명']==scLine].groupby('날짜').sum()
df3 = df3.reset_index()

# df4 = pd.merge(df3, df1, on='날짜')
# print(df4)

df4 = pd.merge(df3[['날짜', '승차']], df1[['날짜', '일강수량']], on='날짜')
# df4 = df4.set_index('날짜', drop=True)

df4 = df4[ (df4['날짜'] >='20210501') & (df4['날짜'] <= '20210531') ]

# plt.figure(figsize=(10, 5))
# plt.plot(df4['날짜'], df4['승차'])
# # plt.show()

# plt.figure(figsize=(10, 5))
# plt.plot(df4['날짜'], df4['일강수량'])
# plt.show()

## 산점도
plt.style.use('ggplot')
df4.plot(kind='scatter', x='일강수량', y='승차', c='coral', s=10, figsize=(10,5))
plt.title('일일 강수량 VS 지하철 승차인원')

plt.show()