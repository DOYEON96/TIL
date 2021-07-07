import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import csv


font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

##

def csv_reset(fn):

    f = open('./multi/0706/subway/'+fn, encoding='utf-8')
    data = csv.reader(f)

    next(data)
    data_lst = []
    for row in data:
        data_lst.append(row[:6])

    df = pd.DataFrame(data_lst, columns=['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'])
    df.to_csv('./multi/0706/retouch/'+fn, encoding = 'cp949', index = False)
    f.close()

##
def file_read():

    filepath = './multi/0706/subway/'
    filename = os.listdir(filepath)

    df1 = pd.DataFrame()
    df3 = pd.DataFrame()
    df4 = []

    for fn in filename:
        try:
            df2 = pd.read_csv(filepath+fn, encoding='cp949')
            
        except:
            csv_reset(fn)
            filepath = './multi/0706/retouch/'
            df2 = pd.read_csv(filepath+fn, encoding='cp949')
            ####
            # df2 = pd.read_csv(filepath+fn, encoding='UTF-8')
            # df2.reset_index(inplace=True)
            # df2 = df2.iloc[:,:-1]
            # df2.columns = ['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자']
            # df2.to_csv('./multi/0706/subway'+fn, encoding='cp949', index=False)
            ####
            
            
        df1 = pd.concat([df1, df2], ignore_index=True)
    return df1

def subway_sch(name):
    df2 = df1[df1['역명'] == name]
    # print(df2)
    df2.plot(x='사용일자', y = '승차총승객수', figsize=(10, 8))
    plt.show()
    # print('')

df1=file_read()
df1 = df1.astype({'승차총승객수':'int64', '사용일자':str, '하차총승객수':'int64'})

print(df1)

subway_name = input("조회할 역 이름을 입력하세요 : ")
df2 = subway_sch(subway_name)

###