import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
from tqdm import tqdm
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def url_parser(sDate, eDate, row = 10):
    usr_key = # 코드
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=' + usr_key
    url = url + '&pageNo=1'
    url = url + '&numOfRows=' + str(row)
    url = url + '&startCreateDt=' + str(sDate)
    url = url + '&endCreateDt=' + str(eDate)

    xml_soup = requests.get(url)
    if xml_soup.status_code != 200:
        exit()
    soup = bs(xml_soup.text, 'html.parser')

    return soup


def covid_info(soup):
    items = soup.find_all('item')

    covid_list = []
    for item in tqdm(items):
        std = item.find('stdday').get_text()    # 기준일
        dt = std[0:4] + std[6:8] + std[10:12]
        dat = datetime.datetime.strptime(dt, "%Y%m%d") + datetime.timedelta(days=-1)
        # std = datetime.datetime.strftime(dat, '%Y%m%d')

        gubun = item.find('gubun').get_text()   # 지역명
        incdec = item.find('incdec').get_text() # 당일 확진자
        defcnt = item.find('defcnt').get_text() # 누적확진자
        localcnt = item.find('localocccnt').get_text()    # 당일 지역 확진 localocccnt
        overcnt = item.find('overflowcnt').get_text()    # 당일 해외 확진

        covid_list.append( [dat, gubun, incdec, localcnt, overcnt, defcnt] )

    df1 = pd.DataFrame(covid_list, columns=['기준일', '지역명', '당일확진자', '지역확진', '해외확진', '누적확진자'])
    return df1

# sDate = '20210701'
# eDate = datetime.datetime.today().strftime('%Y%m%d')
# print(eDate)

# soup = url_parser(sDate, eDate)
# row = soup.find('totalcount').text
# soup = url_parser(sDate, eDate, row)
# df1 = covid_info(soup)

# df1.sort_values(by ='기준일', inplace=True)

# df1.to_csv('./multi/0714/0701코로나확진자.csv', index=False)

df1 = pd.read_csv('./multi/0714/0701코로나확진자.csv')

# df2 = df1.sort_values(by='기준일', ascending=True)
# print(df1[df1['지역명']=='합계'])

# cloc = input('원하는 지역을 입력해주세요 : ')

# df2 = df1[df1['지역명']=='합계']
# df3 = df1[df1['지역명']==cloc]

# df2 = df2.reset_index(drop=True)
# print(df2)
# print(df3)
# plt.style.use('ggplot')
# plt.figure(figsize=(14, 5))

# plt.plot(df2.기준일, df2['당일확진자'], marker='o', markersize=3, label = '합계')
# plt.show()
# plt.plot(df3.기준일, df3['당일확진자'], marker='o', markersize=3, label = cloc)
# plt.legend()
# plt.show()

## 미션 합계부터 각 지역별 차트 출력
# - 차트 제목 출력 : 지역명으로 출력하되 합계는 전체로 출력

plt.style.use('ggplot')
fig = plt.figure(figsize=(15, 15))

# print(df2[df2['지역명'] == '합계'])

# print(df1['지역명'].unique())

# i = 1

# for loc in df1['지역명'].unique():
    
#     df = df1[df1['지역명']==loc]
#     fig.add_subplot(len(df1['지역명'].unique()), 1, i)

#     if loc == '합계':
#         plt.plot(df.기준일, df['당일확진자'], marker='o', markersize=3, label = '전체')
#     else:
#         plt.plot(df.기준일, df['당일확진자'], marker='o', markersize=3, label = str(loc))
#     plt.legend(loc='best')
#     i+=1

# plt.show()

# for loc in df1['지역명'].unique():
    
#     df = df1[df1['지역명']==loc]

#     if loc == '합계':
#         plt.plot(df.기준일, df['당일확진자'], marker='o', markersize=3, label = '전체')
#     else:
#         plt.plot(df.기준일, df['당일확진자'], marker='o', markersize=3, label = str(loc))
    
#     plt.legend(loc='best')
    
#     i+=1
# plt.show()

# 수도권(서울/경기/인천)과 나머지 지역에 대한 분석
# - 일자별 수도권 합계/나머지 데이터에 합계 차트 출력

df2 = df1[df1['지역명']!='합계']
df2 = df2.reset_index(drop=True)

# print(df2.loc[0,'기준일'])
# print(dt_range[0].strftime('%Y-%m-%d'))

# print(df2.loc[18,:])

u_loc = df2['지역명'].unique()
u_dt = df2['기준일'].unique()

print(u_dt)
print(u_loc)