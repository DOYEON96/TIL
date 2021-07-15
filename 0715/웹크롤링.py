from bs4 import BeautifulSoup as bs
import requests
import sys

# url = "https://comic.naver.com/webtoon/weekday.nhn"
# res = requests.get(url)
# res.raise_for_status()

# soup = bs(res.text, "lxml")

# # 네이버 웹툰 전체 목록 가져오기
# cartoons = soup.find_all("a", attrs = {"class":"title"}) # class가 title인 a 엘리먼트를 반환
# for cartoon in cartoons:
#     print(cartoon.get_text())


# 네이버 뉴스 검색 크롤링

url = 'https://search.naver.com/search.naver?query=%EC%BD%94%EB%A1%9C%EB%82%98'
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, 'lxml')
# news_lst = soup.find('ul', attrs ={'class':'list_news'})
li_soup = soup.find_all('div', class_='news_area')

news_lst = []

# li = li_soup.find('a', class_='api_txt_lines dsc_txt_wrap').text
for row in li_soup:
    tit = row.find("a", class_='news_tit').get_text()
    news = li_soup.find('a', class_='api_txt_lines dsc_txt_wrap').get_text()
    news_lst.append({'제목':tit, '내용':news})
    print(tit, news)


# print(li)

## 뉴스제목과 내용 두가지 출력

