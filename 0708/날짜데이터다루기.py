from tqdm import tqdm
import pandas as pd
import datetime
from datetime import timedelta
import API를활용한지하철탑승현황분석 as ap

# sDt = input('조회 시작일을 입력해주세요(yyyymmdd 형식) : ')
# eDt = input('조회 시작일을 입력해주세요(yyyymmdd 형식) : ')

# dtime = datetime.datetime.strptime(sDt, "%Y%m%d") # 문자열을 날짜형자료로 변환 strptime
# dtime2 = datetime.datetime.strptime(eDt, "%Y%m%d")
# print(dtime)

# stime= dtime.strftime("%y-%m-%d") # 날짜형 자료를 문자열 자료로 변환 strftime
# print(stime)

# ptime = dtime2 - dtime
# print(ptime.days)
# print(type(ptime.days))
# print(ptime.seconds)

# print(datetime.datetime.now())
# print(datetime.datetime.now()-datetime.datetime.strptime("20210515", "%Y%m%d"))


# 미션 : 두 문자형 날짜를 입력 받아 두 날짜에 대한 일자차 구하기

sDt='20210223'
eDt = '2021-03-12'
    
dtime = datetime.datetime.strptime(sDt, "%Y%m%d") # 문자열을 날짜형자료로 변환 strptime
dtime2 = datetime.datetime.strptime(eDt, "%Y-%m-%d")

d_d = dtime2 - dtime

print(d_d.days)

# 미션2 : 시작일/종료일 입력

# - 중간날짜 모두 생성하기

######################################################################

# sdt = input("시작할 날짜를 입력해주세요 : ")
# edt = input("종료할 날짜를 입력해주세요 : ")

# sdtime = datetime.datetime.strptime(sdt, "%Y%m%d")
# edtime = datetime.datetime.strptime(edt, "%Y%m%d")

# ddis = edtime - sdtime

# date_lst = []

# for i in tqdm(range(1, ddis.days)):
    
#     cdate = datetime.datetime.strftime(sdtime + timedelta(days=i),"%Y%m%d")
#     date_lst.append(cdate)

# print(date_lst)


####################################################################

sdt = input("시작할 날짜를 입력해주세요 : ")
edt = input("종료할 날짜를 입력해주세요 : ")

dt_index = pd.date_range(start=sdt, end=edt)
dtList = dt_index.strftime("%Y%m%d").tolist()

df0 = ap.main_api(dtList)
print(df0)