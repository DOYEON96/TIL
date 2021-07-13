# 지역별 축제 현황[각자 코딩]
# 주소를 " " 기준으로 나누어 첫번째 값 선택
# 해당 값을 이용해서 '지역' 열 생성 및 데이터 추가
# 지역별 축제 현황 분석(현황 테이블화, 시각화-막대그래프, 원그래프, *히트맵 그래프)


import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

df1 = pd.read_csv('./multi/0713/tour_20190101_20211231.csv')


for row in range(len(df1)):
    if df1.loc[row, '행사주소'] == '온라인개최':
        df1.loc[row, '지역'] = '온라인개최'
    else:
        if df1.loc[row,'행사주소'].split(' ')[0] == '강원':
            df1.loc[row, '지역'] = '강원도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '경남':
            df1.loc[row, '지역'] = '경상남도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '경북':
            df1.loc[row, '지역'] = '경상북도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '대구':
            df1.loc[row, '지역'] = '대구광역시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '백종원':
            df1.loc[row, '지역'] = '충청남도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '부산':
            df1.loc[row, '지역'] = '부산광역시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '서울':
            df1.loc[row, '지역'] = '서울특별시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '서울시':
            df1.loc[row, '지역'] = '서울특별시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '세종':
            df1.loc[row, '지역'] = '세종특별자치시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '울산':
            df1.loc[row, '지역'] = '울산광역시'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '전남':
            df1.loc[row, '지역'] = '전라남도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '제주':
            df1.loc[row, '지역'] = '제주특별자치도'
        elif df1.loc[row,'행사주소'].split(' ')[0] == '충북':
            df1.loc[row, '지역'] = '충청북도'
        else:
            df1.loc[row, '지역'] = df1.loc[row,'행사주소'].split(' ')[0]
    
# print(df1)

df1 = df1[(df1['지역']!='온라인개최') & (df1['지역']!='비대면개최')]
df2 = df1.groupby(['지역'])['행사명'].count()

df2 = df2.reset_index()
df2.columns = ['지역', '행사횟수']

# print(df2)
df2.plot.bar()
plt.show()
# print(x)
# print(df2.iloc[:])
plt.pie(df2['행사횟수'],labels=df2['지역'], autopct='%.1f%%')
plt.show()

# print(df2)