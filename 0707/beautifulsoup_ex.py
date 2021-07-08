# Beautifulsoup

from bs4 import BeautifulSoup as bs

html_str = '''
<html>
    <head>
        <meta charset="UTF-8">
        <title>김도연의 홈페이지</title>
    </head>
    <body>
        <h1>안녕하세요 김도연입니다.</h1>
        <input type="text", value="아이디를 입력하세요">
        <input type="password">
        <input type="button", value="로그인">
        <a href="http://google.com">구글로 이동하기</a>
    </body>
</html>
'''

html_str2 = '''
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
        <div>
            <ul>
                <li>open</li>
                <li>close</li>
            </ul>
        </div>
    </body>
</html>

'''

soup = bs(html_str2, 'html.parser')

print(soup)

# print(soup.find('ul')) # find('태그명') 대상 태그를 찾아 그 중 첫번째 값을 가져온다.

print(soup.find('ul', class_="reply")) # class명이 reply인 ul 태그 값을 가져온다.

print(soup.find_all('ul')) # soup 내의 모든 ul태그 값을 가져옴
print(soup.find_all('ul')[-1]) # 인덱싱도 가능

html_txt=soup.find_all('ul')
print(html_txt[-1])

# 태그를 제거하고 태그가 가지고 있는 텍스트 값 출력

print(html_txt[-1].text)        # text 속성값 출력
print(html_txt[-1].get_text())  # get_text() 함수 이용

html_txt=soup.find_all('li')
print(html_txt)

for txt in html_txt:
    print(txt.text)