# [과제]

# 1. 공공데이터활용지원센터_보건복지부 코로나19 연령별·성별감염 현황 api연결
# 2. 데이터 : 등록일, 성별구분, 누적확진자, 사망자
# 3. 연령별, 성별 데이터 DataFrame 형식으로 변경
# 4. 당일 확진자 열 추가(당일누적확진자-전일누적확진자)
# 5. 구분(성별/연령별) 시각화(x축 : 날짜, y축 : 조회값)
# 6. 날짜별 행/열 변경(by 당일확진자)
# 기간 : 시작일/종료일 입력받아 수행

import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
from datetime import datetime, timedelta
import matplotlib.font_manager as fm

font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def url_parse(sDate, eDate, row=10):
    usr_key = # 코드
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson?serviceKey='+ usr_key
    url = url + '&pageNo=2'
    url = url + '&numOfRows=' + str(row)
    url = url + '&startCreateDt=' + str(sDate)
    url = url + '&endCreateDt=' + str(eDate)

    res = requests.get(url)
    res.raise_for_status()
    soup = bs(res.text, 'lxml')

    return soup

def covid_info(sDate, eDate, soup):

    items = soup.find_all('item')

    dt_lst = []

    for item in tqdm(items):
        date = item.find('createdt').get_text()[:10] # 기준일
        conf = item.find('confcase').get_text() # 누적확진자수
        death = item.find('death').get_text() # 누적사망자수
        gubun = item.find('gubun').get_text() # 연령/성별 구분

        dt_lst.append([date, gubun, conf, death])
        df = pd.DataFrame(dt_lst, columns=['기준일', '구분', '누적확진자수', '누적사망자수'])
        
    df = df.astype( {'누적확진자수':int, '누적사망자수':int})
    return df

def gender_today_conf(df): # 남녀 당일 확진자수 계산, 추가 함수

    df['당일확진자수'] = 0 # 당일확진자수 열 생성 후 초기화
    df.reset_index(drop=True, inplace=True) # 인덱스 정렬
    

    for i in range(len(df)-1):
        df.loc[i, '당일확진자수'] = df.loc[i, '누적확진자수'] - df.loc[i+1, '누적확진자수']

    df.sort_values('기준일', inplace=True, ignore_index=True)
    df = df[df['기준일']!=ysd]

    return df

def age_today_conf(df): # 연령대별 당일 확진자수 계산, 추가 함수

    df['당일확진자수'] = 0 # 당일확진자수 열 생성 후 초기화
    df.reset_index(drop=True, inplace=True) # 인덱스 정렬
    
    
    for i in range(9): # 연령대별 반복
        for j in range(i, len(df)-9, 9): # 연령대별 계산
            df.loc[j, '당일확진자수'] = df.loc[j, '누적확진자수'] - df.loc[j+9, '누적확진자수']

    df.sort_values('기준일', inplace=True, ignore_index=True)
    df = df[df['기준일']!=ysd]

    return df

def gender_df_sch(df, df2):

    plt.figure(figsize=(15, 5))
    plt.plot(df['기준일'], df['당일확진자수'], label='남성')
    plt.plot(df2['기준일'], df2['당일확진자수'], label='여성')

    plt.title('남/녀 확진자수')
    plt.legend()
    plt.show()

def age_df_sch(df):
    plt.figure(figsize=(15,5))

    idx = df['구분'].unique()

    for i in range(len(idx)):
        df1 = df[df['구분']==idx[i]]
        plt.plot(df1['기준일'], df1['당일확진자수'], label=idx[i])

    plt.title('연령대별 확진자수')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    sDate = input('시작일을 입력해주세요 : ')
    eDate = input('종료일을 입력해주세요 : ')

    sDate = datetime.strptime(sDate, "%Y%m%d") + timedelta(days=-1)
    sDate = datetime.strftime(sDate, '%Y%m%d')

    ysd = sDate[0:4] + '-' + sDate[4:6] + '-' + sDate[6:] # 원하는 날짜 하루전(시작날짜 당일 데이터 계산 후 전날 데이터 삭제를 위해)

    soup = url_parse(sDate, eDate) # 파싱
    df1 = covid_info(sDate, eDate, soup) # 원하는 데이터만 데이터프레임화
    
    df2 = df1[df1['구분']=='남성'] # 남성 확진자수 데이터 프레임
    df3 = df1[df1['구분']=='여성'] # 여성 확진자수 데이터 프레임
    df1 = df1[(df1['구분']!='남성') & (df1['구분']!='여성')] # 연령대별 데이터프레임

    df1 = age_today_conf(df1)       # 데이터프레임별 당일 확진자수 열 생성 및 값 추가 함수 실행
    df2 = gender_today_conf(df2)
    df3 = gender_today_conf(df3)

    # df1.sort_values('기준일', inplace=True, ignore_index=True) # 일자 오름차순 정렬
    # df2.sort_values('기준일', inplace=True, ignore_index=True)
    # df3.sort_values('기준일', inplace=True, ignore_index=True)

    # sDate의 전날 데이터 삭제
    # df1 = df1[df1['기준일']!=ysd]
    # df2 = df2[df2['기준일']!=ysd]
    # df3 = df3[df3['기준일']!=ysd]


    # df1.to_csv('./multi/0715/data/final.csv', index=False)
    # df2.to_csv('./multi/0715/data/final2.csv', index=False)
    # df2.to_csv('./multi/0715/data/final3.csv', index=False)

    

    cho = input('조회할 방법을 선택해주세요(성별/연령별) : ')

    if cho == '성별':
        gender_df_sch(df2, df3)
    elif cho == '연령별':
        age_df_sch(df1)
    else:
        print('성별/연령별 중에 선택해주세요')