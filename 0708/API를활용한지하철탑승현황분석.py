from tqdm import tqdm
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pandas as pd

def url_print(tdate, uRow=3):

    user_key = '4d46754e4c646f7934376e4342554e'

    d_type = 'xml'
    api_name = 'CardSubwayStatsNew'
    first_row = '1'
    end_row = str(uRow)
    d_date = str(tdate)

    url = 'http://openapi.seoul.go.kr:8088/' + user_key + '/' + d_type + '/' + api_name + '/' + first_row + '/' + end_row + '/' + d_date

    return url

def url_parse(url):
    subway_xml = requests.get(url)
    if subway_xml.status_code == 200:
        subway_soup = bs(subway_xml.text, 'html.parser')
        
        # print(subway_soup)
    else:
        print('데이터 접근에 실패했습니다.')
        exit()

    return subway_soup

def seoul_sw_pandas(seoul_sw_soup):
    xml_row = seoul_sw_soup.find_all('row')
    xml_txt = []
    for row in xml_row:
        dt = row.find('use_dt').text
        line = row.find('line_num').text
        sub_sta = row.find('sub_sta_nm').text
        ride = row.find('ride_pasgr_num').text
        alight = row.find('alight_pasgr_num').text

        xml_txt.append({'사용일': dt, '라인': line, '역명': sub_sta, '승차': ride, '하차': alight})

    #print(xml_txt)
    df = pd.DataFrame(xml_txt)
    return df

def main_api(dtList):
    df0 = pd.DataFrame()
    for sdt in tqdm(dtList):
        seoul_sw_soup = url_print(sdt)
        urow = url_parse(seoul_sw_soup).find('list_total_count').text
        seoul_sw_soup=url_print(sdt, urow)
        parse_url=url_parse(seoul_sw_soup)

        df = seoul_sw_pandas(parse_url)

        df0=pd.concat([df0, df], ignore_index=True)

    return df0

##################################################

# user_key = '4d46754e4c646f7934376e4342554e'

# d_type = 'xml'
# api_name = 'CardSubwayStatsNew'
# first_row = '1'
# end_row = '5'
# d_date = '20151101'

# url = 'http://openapi.seoul.go.kr:8088/' + user_key + '/' + d_type + '/' + api_name + '/' + first_row + '/' + end_row + '/' + d_date

# print(url)

##################################################

# s_date = input('조회를 원하는 날짜를 입력해주세요(yyyymmdd 형식) : ')
# url = url_print(s_date) # 원하는 날짜를 조회
# end_row = url_parse(url) # 원하는 날짜 데이터의 전체행 갯수를 확인
# u_row = end_row.find('list_total_count').text
# end_url = url_print(s_date, u_row) # 원하는 날짜의 전체행 데이터를 확인

# seoul_sw_soup = url_parse(end_url)

# df = seoul_sw_pandas(seoul_sw_soup)
# print(df)

# url = url_print(20210704)
# print(url_parse(url))