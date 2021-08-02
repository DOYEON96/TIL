from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from tqdm import tqdm
from konlpy.tag import Okt
from collections import Counter
from textblob.classifiers import NaiveBayesClassifier

def url_parse():
    url = 'https://play.google.com/store/apps/details?id=com.coupang.mobile&showAllReviews=true'
    driver.get(url)
    driver.implicitly_wait(5)

    for i in range(1, 30):
        time.sleep(2)
        driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
        
        if (i % 5) == 0:
            
            driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span').click()
            
            
        time.sleep(1)
    
    txt = driver.find_elements_by_class_name('UD7Dzf')
    print(len(txt))
    
    lst = []

    for j in range(1, len(txt) + 1):
        lst.append(driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div/div['+str(j)+']/div/div[2]/div[2]/span[1]').text)

    return lst



## 


f = open('./multi/0727/data/test.txt', 'r', encoding='utf-8')
txt = f.read()
f.close

okt = Okt()

okt.pos
pos = okt.pos(txt)

cnt = Counter(pos)
