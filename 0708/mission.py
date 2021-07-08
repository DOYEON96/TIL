from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pandas as pd
from tqdm import tqdm

def url_print(tdate, uRow=3):

    user_key = #코드

    d_type = 'xml'
    api_name = 'CardSubwayPayFree'
    first_row = '1'
    end_row = str(uRow)
    d_date = str(tdate)

    url = 'http://openapi.seoul.go.kr:8088/' + user_key + '/' + d_type + '/' + api_name + '/' + first_row + '/' + end_row + '/' + d_date

    return url

def url_parse(url):
    subway_xml = requests.get(url)
    if subway_xml.status_code == 200:
        subway_soup = bs(subway_xml.text, 'html.parser')
    else:
        print('데이터 접근에 실패했습니다.')
        exit()

    return subway_soup

def seoul_sw_pandas(seoul_sw_soup):
    if seoul_sw_soup.find('CODE') == 'INFO-200':
        print(seoul_sw_soup.find('MESSAGE').text)
        exit()
    xml_row = seoul_sw_soup.find_all('row')
    xml_txt = []
    for row in xml_row:
        mon = row.find('use_mon').text
        line = row.find('line_num').text
        sub_sta = row.find('sub_sta_nm').text
        pay_ride_num = row.find('pay_ride_num').text
        free_ride_num = row.find('free_ride_num').text
        pay_alight_num = row.find('pay_alight_num').text
        free_alight_num = row.find('free_alight_num').text

        xml_txt.append({'사용일': mon, '호선명': line, '지하철역': sub_sta, '유임승차인원': pay_ride_num, '무임승차인원': free_ride_num, '유임하차인원': pay_alight_num, '무임하차인원': free_alight_num})

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


sdt = input("시작할 연도를 입력해주세요 : ")
edt = input("종료할 연도를 입력해주세요 : ")

dt_index = pd.date_range(start = sdt, end = str(int(edt) + 1) ,freq='M')
dtList = dt_index.strftime("%Y%m").tolist()

df0 = main_api(dtList)
df0.to_csv('./multi/0708/'+sdt+'_'+edt+'지하철데이터.csv', index=False)