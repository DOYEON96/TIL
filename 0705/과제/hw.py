### [년도별 외국인 현황 분석]
### 1. 사용자가 입력된 년도의 데이터를 이용해 외국인 현황
### 2. x축으로 자치구 사용
### 3. 막대그래프, 제목, x/y 축제목
### 4. 외국인 남성/여성의 구성 비율(자치구별 확인)


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df1=pd.read_csv('./multi/0705/data/report.txt', sep ='\t', header=1)
df1 = df1.iloc[:, [0,1,7,8,10,11]]
df1.drop(0, inplace=True)

col_name=['년도', '자치구', '내국인(남)', '내국인(여)','외국인(남)','외국인(여)']
df1.columns = col_name

df1=df1[df1['내국인(남)']!="…"]

for i in range(2, len(df1.columns)):
    df1.iloc[:,i] = df1.iloc[:,i].str.replace(',','')

df1=df1.astype( {'내국인(남)':int,'내국인(여)':int,'외국인(남)':int,'외국인(여)':int} )

ch = input("원하는 조건을 선택하세요(1 : 년도별, 2 : 자치구별) : ")

if ch == "1":

    ch_2 = '년도별'
    year_in = input("원하는 년도를 입력해주세요(1992 ~ 2020) : ")

    if (int(year_in) < 1992) | (int(year_in) > 2020):
        print('1992년과 2020년 사이에서 입력해주세요')
        exit()

    df2 = df1[(df1['년도']==year_in) & (df1['자치구']!='합계')]
    df2.plot(kind = 'bar', x = '자치구', y = ['외국인(남)', '외국인(여)'], xlabel = '자치구명', ylabel = '외국인 남/녀 인구수', figsize = (10, 8))

    plt.title(year_in + '년도 자치구별 외국인 남/녀 인구 분석')


elif ch == '2':

    ch_2 = '자치구별'
    gu_in = input("원하는 자치구명을 입력해주세요 : ")

    if gu_in not in list(df1['자치구'].unique()):
        print(f'{gu_in}은 존재하지 않습니다.')
        exit()

    df2 = df1[(df1['자치구'] == gu_in) & (df1['자치구']!='합계')]
    df2.plot(kind='bar', x = '년도', y = ['외국인(남)', '외국인(여)'], xlabel = '년도', ylabel = '외국인 남/녀 인구수', figsize = (10, 8))

    plt.title(gu_in + ' 년도별 외국인 남/녀 인구 분석')

else:
    print('1과 2중 선택해주세요')
    exit()

plt.legend(loc='best')
plt.show()