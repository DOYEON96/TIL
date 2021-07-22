import requests
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import sys
from tqdm import tqdm


def news_parse(keyword, sPage=1, ePage=1):

    for page in range(int(sPage), int(ePage)+1):
        
        # 'http://www.kmib.co.kr/search/searchResult.asp?searchWord=%uC190%uD765%uBBFC&pageNo=1'

        url = 'http://www.kmib.co.kr/search/searchResult.asp?searchWord=' + quote(keyword)
        # url = url + '&pageNo=' + str(page)
        
        res = requests.get(url)
        res.raise_for_status()

        soup = bs(res.text, 'lxml')

        return url
    
url = news_parse('손흥민', 1, 2)
print(url)
