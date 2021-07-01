# import csv

# f = open("./multi/0630/data/seoul.csv") # 뒤의 두 파라미터 기본값 지정, "r" 읽기모드.

# data = csv.reader(f)
# header=next(data) # 첫 번째 행(칼럼명), header에 저장

# max_temp = 0
# max_day = ""

# for row in data:
#     if row[4]!="":
#         if float(row[4])>max_temp:
#             max_temp=float(row[4])
#             max_day=row[2]

# print(f"최고기온 : {max_temp}, 날짜 : {max_day}")

##########################################################################
# from matplotlib import rc
# import matplotlib.pyplot as plt
# import csv

# font_path="C:/Windows/Fonts/malgun.ttf"
# font_name=fm.FontProperties(fname=font_path)

# f = open("./multi/0630/data/seoul.csv", encoding='cp949') # 뒤의 두 파라미터 기본값 지정, "r" 읽기모드.

# data = csv.reader(f)
# header=next(data) # 첫 번째 행(칼럼명), header에 저장

# max_temp = []  # 최고기온
# min_temp = []   # 최저기온
# year_temp = []  # 생일자 년도

# for row in data:
#         if int(row[2].split("-")[0]) >= 1985 and row[4] != "":
#             if row[2][-5:]=="04-06":
#                 max_temp.append(float(row[4]))
#                 min_temp.append(float(row[6]))
#                 year_temp.append(row[2].split("-")[0])

# plt.figure(figsize=(14, 5))

# plt.rc('font', family='malgun Gothic')

# plt.plot(year_temp, max_temp, label="최고기온", color="r")
# plt.plot(year_temp, min_temp, label="최저기온", color="b")
# plt.title("내 생일날 기온 변화")
# plt.legend(loc="best")
# plt.show()

###################################################################
# 미션 : 평균데이터를 이용한 날짜별 차트 출력
# 1. 1960년 이후 8월 15일 편균기온 데이터로 차트 작성
# 2. 1960년 이후 1월 15일 평균기온 데이터로 차트 작성

# from matplotlib import rc
# import matplotlib.pyplot as plt
# import csv

# f = open("./multi/0630/data/seoul.csv", encoding='cp949') # 뒤의 두 파라미터 기본값 지정, "r" 읽기모드.

# data = csv.reader(f)
# header=next(data) # 첫 번째 행(칼럼명), header에 저장

# temp115 = []
# temp815 = []
# yeartmp = []

# for row in data:
#         if int(row[2].split("-")[0]) >= 1960 and row[3] != "" and int(row[2].split("-")[0]) < 2021:
#             if row[2][-5:]=="08-15":
#                 temp815.append(float(row[3]))
#             elif row[2][-5:]=="01-15":
#                 temp115.append(float(row[3]))
#                 yeartmp.append(row[2].split("-")[0][-2:])

# plt.rc('font', family='malgun Gothic')
# plt.rcParams['axes.unicode_minus'] = False

# plt.plot(yeartmp, temp815, label="8월 15일 평균 온도", color="r")
# plt.plot(yeartmp, temp115, label="1월 15일 평균 온도", color="b")
# plt.title("1월 15일과 8월 15일 평균온도")
# plt.legend()
# plt.show()

############################################################################
# 히스토그램 
# -주사위를 굴린다, n 번반복, 주사위 눈의 횟수를 히스토그램으로 그림
import matplotlib.pyplot as plt
import random

# clist = []
# cnt1=0;cnt2=0;cnt3=0;cnt5=0;cnt4=0;cnt6=0
# for i in range(100):

#     num = random.randint(1,6)
#     clist.append(num)

#     if num == 1:
#         cnt1+=1
#     elif num == 2:
#         cnt2+=1
#     elif num == 3:
#         cnt3+=1
#     elif num == 4:
#         cnt4+=1
#     elif num == 5:
#         cnt5+=1
#     else:
#         cnt6+=1

# print(f"1 : {cnt1}회, 2 : {cnt2}회, 3 : {cnt3}회, 4 : {cnt4}회, 5 : {cnt5}회, 6 : {cnt6}회")
# plt.hist(clist)
# plt.show()

###################################################333

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71, 80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
weight2 = [52, 67, 84, 66, 58, 78, 71, 57, 76, 62, 51, 79, 69, 64, 76, 57, 63, 53, 79, 64, 50, 61]
plt.hist((weight, weight2), histtype='bar')
plt.title('histtype - bar')
plt.figure()

plt.hist((weight, weight2), histtype='barstacked')
plt.title('histtype - barstacked')
plt.figure()

plt.hist((weight, weight2), histtype='step')
plt.title('histtype - step')
plt.figure()

plt.hist((weight, weight2), histtype='stepfilled')
plt.title('histtype - stepfilled')
plt.show()
