from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

user_key = 코드
url = 'http://openapi.seoul.go.kr:8088/'+user_key+'/xml/CardSubwayStatsNew/1/5/20151101'

# 공공API

# - requests 라이브러리는 매우 직관적인 API를 제공
# - 어떤 방식의 http요청을 하느냐에 따라서 해당하는 이름의 함수를 사용
# - get방식 : requests.get()
# - post방식 : requests.post()
# - put방식 : requests.put()
# - delete방식 : requests.delete()

xml = requests.get(url)
print(xml.status_code)