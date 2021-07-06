import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


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
            df2 = pd.read_csv(filepath+fn, encoding='UTF-8')
            df2.reset_index(inplace=True)
            df2 = df2.iloc[:,0:-1]
            df2.columns = ['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자']
            
            
        df1 = pd.concat([df1, df2], ignore_index=True)
    return df1

def subway_sch(name):
    df2 = df1[df1['역명'] == name]
    df2.plot(x='사용일자', y = '승차총승객수', kind='bar')
    plt.show()
    # print('')

df1=file_read()
print(df1)
subway_name = input("조회할 역 이름을 입력하세요 : ")
df2 = subway_sch(subway_name)