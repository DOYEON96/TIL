# Selenium을 이용한 브라우저 제어

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import pyperclip

url='https://www.naver.com/'
driver = webdriver.Chrome('./chromedriver.exe')

keys=Keys()
time.sleep(2)
driver.get(url)
# login_click()   # 로그인 함수
# time.sleep(2)

# 검색 창 열고 코로나 입력후 검색
# driver.find_element_by_xpath('//*[@id="query"]').click()
# time.sleep(2)

# qinput = driver.find_element_by_xpath('//*[@id="query"]')
# qinput.send_keys('코로나')
# qinput.send_keys(keys.ENTER)
# time.sleep(2)

#################################################

# 로그인창
driver.get(url)
driver.find_element_by_xpath('//*[@id="account"]/a').click()
time.sleep(2)

tag_id = driver.find_element_by_id('id') # 아이디 입력란 객체 정의
tag_pw = driver.find_element_by_id('pw') # 비밀번호 입력란 객체 정의

tag_id.clear()
tag_id.click()
time.sleep(1)
pyperclip.copy('')
tag_id.send_keys(keys.CONTROL, 'v')
time.sleep(2)

tag_pw.clear()
tag_pw.click()
time.sleep(1)
pyperclip.copy('')
tag_pw.send_keys(keys.CONTROL, 'v')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="log.login"]').click()