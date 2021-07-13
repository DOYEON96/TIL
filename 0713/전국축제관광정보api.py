import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime
import seaborn as sns

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


def url_parser(sDate, eDate, row = 10):
    user_key = #코드

    url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival?serviceKey=' + user_key
    url = url + '&MobileOS=ETC&MobileApp=AppTest&arrange=A&listYN=Y' # 기본 옵션
    url = url + '&numOfRows=' + str(row) # 한페이지 출력데이터 개수
    url = url + '&eventStartDate=' + str(sDate) # 조회 시작일 
    url = url + '&eventEndDate=' + str(eDate) # 조회 마지막일

    xml_soup = requests.get(url)
    if xml_soup.status_code != 200:
        print('데이터를 불러올 수 없습니다.')
        exit()
    else:
        soup = bs(xml_soup.text, 'html.parser')
        # print(url)
    return soup

def tour_info(sDate, eDate, soup):
    # 파싱한 데이터 중 원하는 데이터 추출
    row = soup.find('totalcount').text
    tour_soup = url_parser(sDate, eDate, row)
    
    items = tour_soup.find_all('item')

    df_lst = []
    for i in tqdm(items):
        sdate = i.find('eventstartdate').get_text() # 시작일
        edate = i.find('eventenddate').get_text() # 종료일
        tit =  i.find('title').get_text() # 행사명
        try:
            addr = i.find('addr1').get_text() # 행사주소
            
        except:
            addr = '온라인개최'
        try:
            tel = i.find('tel').get_text() # 연락처
        except:
            tel = '-'
        try:
            mapx = i.find('mapx').get_text() # y 좌표(위도)
            mapy = i.find('mapy').get_text() # x 좌표(경도)
        except:
            mapx = ''
            mapy = ''
            
        
        df_lst.append( {'시작일':sdate, '종료일':edate, '행사명':tit, '행사주소':addr, '연락처':tel, '위도':mapy, '경도':mapx} )

        df = pd.DataFrame(df_lst)

    return df


# sDate = 20210101
# eDate = 20211231

# sDate = input('조회 시작일을 입력해주세요(yyyymmdd) : ')
# eDate = input('조회 종료일을 입력해주세요(yyyymmdd) : ')

# soup = url_parser(sDate, eDate)
# df1 = tour_info(sDate, eDate, soup)
# df1.to_csv('./multi/0713/tour_'+str(sDate)+'_'+str(eDate)+'.csv', index=False)
df1 = pd.read_csv('./multi/0713/tour_20190101_20211231.csv')

### 축제 데이터 분석
# - 2020~2021년 축제 건수 비교
# - 축제유형(집합/비대면)
# - 지역별 축제 현황

# df1['시작년'] = df1['시작일'].str[:4]
# df2 = df1.groupby('시작년')['행사명'].count()

# df2.plot.bar()
# plt.show()

df1 = df1.astype( {'시작일':str, '종료일':str} )
# print(df1.info())
df1['시작일'] = pd.to_datetime(df1['시작일'],format="%Y%m%d")
df1['종료일'] = pd.to_datetime(df1['종료일'],format="%Y%m%d")
df1['시작년'] = df1['시작일'].dt.year
df1['시작월'] = df1['시작일'].dt.month

# print(df1)

df2 = df1.groupby(['시작년', '시작월'])['행사명'].count()
df2 = df2.reset_index()

df2 = pd.concat([df2[df2['시작년']==2021].set_index('시작월'), df2[df2['시작년']==2020].set_index('시작월')], axis = 1)
df2 = df2.fillna(0)
df2 = df2.astype( {'시작년':int, '행사명':int} )

df2.columns = ['2021년', '', '2021년', '']

on2020 = df1[(df1['시작년']==2020)&(df1['행사주소']!='온라인개최')]['행사명'].count()
off2020 = df1[(df1['시작년']==2020)&(df1['행사주소']=='온라인개최')]['행사명'].count()
on2021 = df1[(df1['시작년']==2021)&(df1['행사주소']!='온라인개최')]['행사명'].count()
off2021 = df1[(df1['시작년']==2021)&(df1['행사주소']=='온라인개최')]['행사명'].count()

d_lst = [[on2020, off2020], [on2021, off2021]]

df3 = pd.DataFrame(d_lst, index=['2020', '2021'], columns=['온라인', '오프라인'])
# df2.plot.bar(rot=0)
# plt.show()

# print(df3)

# x = [10, 30, 20]
# xlab = ['a', 'b', 'c']

# print(df3.dtypes)

# x= list(df3.iloc[0])
# xlab = df3.columns

# plt.pie(x, labels=xlab, autopct="%.1f%%")
# plt.title('2020년')
# plt.show()

fig = plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
x=list(df3.iloc[0])
xlab = df3.columns
plt.pie(x, labels=xlab, autopct="%.1f%%")
plt.title('2020년')

plt.subplot(1, 2, 2)
x=list(df3.iloc[1])
xlab = df3.columns
plt.pie(x, labels=xlab, autopct="%.1f%%")
plt.title('2021년')


# [df2.iloc[0,0], df2.iloc[0, 1]]

# plt.pie(df3['온라인'], df3.index, autopct='%.1f%%')
# plt.show()

######################################################################

## 지역별 축제 현황
# - 주소를 ' ' 기준으로 나누어 첫번째 값 선택
# - 해당 값을 이용해서 '지역' 열 생성 및 데이터 추가
# - 지역별 축제 현황 분석(현황 테이블화, 시각화-막대그래프, 원그래프)

# print(df1['행사주소'].str.split(' '))
# df1['지역'] = df1['행사주소'].str.split(' ')[0]
# print(df1['지역'])


#######################################################################

## 지도에 축제 위치 출력하기
import folium
df1 = df1.fillna(0)
df2 = df1[(df1['위도']!=0) & (df1['시작년']==2021)]

umap = folium.Map(location=[35.94717219388294, 126.97112874673742], zoom_start=15) 

for inx in df2.index:
    folium.Marker(location=[df2.loc[inx,'위도'], df2.loc[inx,'경도']], icon = folium.Icon(color='red'), popup=df2.loc[inx,'행사명']).add_to(umap)
umap.save('./multi/0713/2021년축제정보.html')