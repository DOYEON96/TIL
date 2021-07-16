from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import os
from tqdm import tqdm
import time

keyword = input('검색할 이미지 키워드를 입력해주세요 : ')

url = 'https://www.google.com/search?q=' + keyword
url = url + '&sxsrf=ALeKk016HwVb7XPbQmmm__gyVEjvdD89rQ:1626412202733&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjCnOjM6ebxAhUMAYgKHZzyD9gQ_AUoAXoECAEQAw&biw=1600&bih=757'

driver = webdriver.Chrome()
driver.get(url)

img_url_lst = []

for i in range(10):
    if i == 9:
        driver.find_element_by_css_selector('#islmp > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click()

    driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);"))
    time.sleep(2)

html_source = driver.page_source
soup = bs(html_source, 'lxml')

img_soup = soup.select('img.rg_i.Q4LuWd')

# img_url = img_soup[0]['src']

# srcf='./multi/0716/data/'+keyword+'_1.jpg'
# urllib.request.urlretrieve(img_url, srcf)

img_lst=[]

for img in tqdm(img_soup, desc='링크='):
    try:
        img_lst.append(img['src'])
    except:
        img_lst.append(img['data-src'])

print('중복 제거전 사진수:', len(img_lst))
img_lst = set(img_lst)
print('중복 제거후 사진수:', len(img_lst))

fDir='./multi/0716/data/'
fName=os.listdir(fDir)


save_dir=keyword+'_구글'
fName_dir=keyword+'0'
cnt = 0

while True:
    if keyword not in fName:
        os.makedirs(fDir+fName_dir)
        break
    cnt+=1
    fname_dir = keyword+str(cnt)

print(fName_dir, '로 폴더 생성')

cnt = 0
for img in tqdm(img_lst):
    sfdir = fDir + fName_dir + '/'+keyword+str(cnt)+'.jpg'
    urllib.request.urlretrieve(img, sfdir)
    cnt += 1

driver.close()
print('저장완료')
