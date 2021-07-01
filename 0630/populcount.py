# import csv
# import matplotlib.pyplot as plt
# from matplotlib import rc

# f = open("./multi/0630/data/202105_인구현황.csv")
# data = csv.reader(f)
# header=next(data)

############################################
# for row in data:
#     if "전라" in row[0]:

#         tot_pop=[int(i.replace(",","")) for i in row[3:104]]
#         man_pop=[int(i.replace(",","")) for i in row[106:207]]
#         wom_pop=[int(i.replace(",","")) for i in row[209:]]

############################################
# loc_lst = ['서울', '대전', '대구', '부산', '울산', '인천', '광주']

# plt.rc('font', family='malgun Gothic')

# for row in data:
#     for loc_n in loc_lst:
#         if loc_n in row[0]:
#             tot_pop=[int(i.replace(",","")) for i in row[3:104]]

# ############################################
#             plt.style.use('ggplot')
#             plt.plot(tot_pop, label=loc_n)

#             plt.legend(loc="best")
# plt.show()

# f.close()

##########################################################

# import csv
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm

# font_path="C:/Windows/Fonts/malgun.ttf" 
# font_name=fm.FontProperties(fname=font_path).get_name()
# plt.rc('font', family=font_name)

# loc_lst=['서울', '경기', '부산', '인천', '울산', '광주', '대전', '대구']

# plt.style.use('ggplot')
# plt.figure(figsize=(10,3))

# for loc_n in loc_lst:
#     f = open("./multi/0630/data/202105_인구현황.csv")
#     data=csv.reader(f)
#     for row in data:
#         if loc_n in row[0]:
#             tot_pop=[int(i.replace(",","")) for i in row[3:104]]
    

#     plt.plot(tot_pop, label=loc_n)

#     f.close()

# plt.legend()
# plt.show()

#########################################################

import csv
import matplotlib.pyplot as plt
from matplotlib import rc

f = open("./multi/0630/data/연간_인구현황_시군구별.csv")
data = csv.reader(f)
header=next(data)

alist=[]
blist=[]

for row in data:
    for i in range(3, 28, 3):
        cityname = row[0].split()[-2]
        if i == 12:
            blist+=[alist]
            alist=[]
            alist.append("2019년도")
            alist.append(cityname)
        elif i == 21:
            blist+=[alist]
            alist=[]
            alist.append("2020년도")
            alist.append(cityname)
        elif i == 3:
            alist.append("2018년도")
            alist.append(cityname)
        alist.append(row[i])
    blist+=[alist]
    alist=[]

# print(blist)

plt.plot(blist)
plt.show()