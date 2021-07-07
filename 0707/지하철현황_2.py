import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm
import csv

### 한글 표기
font_name=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)

def Csv_reset(fn):
    ### csv 파일 전처리 함수
    f = open('./multi/0706/subway/'+fn, encoding='utf-8')
    data = csv.reader(f)
    # "사용일자"', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'

    next(data)
    data_lst = []
    for row in data:
        data_lst.append(row[:6])

    df = pd.DataFrame(data_lst, columns=['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수', '등록일자'])
    df.to_csv('./multi/0706/retouch/'+fn, encoding='cp949', index=False)
    f.close()

def file_read():
    ### subway 폴더에 있는 모든 파일 하나로 만들기
    filePath='./multi/0706/subway/'
    fileName=os.listdir(filePath)  # subway 폴더의 모든 파일 및 하위 폴더 정보를 리스트형으로 가져와 저장

    df1=pd.DataFrame()

    for fn in fileName:
        ### try ~ except : 예외처리 구문
        #print(fn)
        try:   # 정상코드 수행
            df2=pd.read_csv(filePath+fn, encoding='cp949')
        except: # try 구문에서 에러 발생시 처리하기 위한 구문
            Csv_reset(fn)
            filePath = './multi/0706/retouch/'
            df2 = pd.read_csv(filePath + fn, encoding='cp949')
        # 데이터 한개의 파일로 만들기
        df1=pd.concat([df1, df2])

    df1=df1.reset_index(drop=True)

    return df1

def subway_sch1(dfdata, subway_name):
    df2=dfdata[dfdata['역명']==subway_name]
    #print(df2.info())
    # df2 = df2.astype({'승차총승객수': 'int64','사용일자':'str'})
    df2.plot(x='사용일자', y='승차총승객수')
    plt.show()

def subway_sch2(dfdata, subway_name):
    ############################################################
    # df2=dfdata[dfdata['역명']==subway_name]
    # #print(df2.info())
    # # df2 = df2.astype({'승차총승객수': 'int64','사용일자':'str'})
    # df2=df2.groupby('사용일자')[['승차총승객수','하차총승객수']].sum()
    # df2.plot()
    # plt.show()

    ##############################################################
    year_in = int(input("조회할 연도를 입력해주세요 : "))
    # month_in = int(input("조회할 월을 입력해주세요 : "))
    df2=dfdata[(dfdata['역명']==subway_name) & (dfdata['년'] == year_in)]

    df2=df2.groupby('일')['승차총승객수'].sum()
    df2.plot()
    plt.show()


def subway_sch3(dfdata, subway_name):
    year_in = int(input("조회할 연도를 입력해주세요 : "))
    # month_in = int(input("조회할 월을 입력해주세요 : "))
    df2=dfdata[(dfdata['역명']==subway_name) & (dfdata['년'] == year_in)]

    df2=df2.groupby('월')['승차총승객수'].sum()
    df2.plot()
    plt.show()

### 사용자 함수 호출 부분
df1=file_read()

# subway_name=input('조회역 입력:')
# subway_sch2(df1, subway_name)

# 데이터 타입 변경
df1=df1.astype({'사용일자':str, "승차총승객수":"int64", "하차총승객수":"int64"})

# 등록일자 열 삭제
df1.drop(['등록일자'], axis=1, inplace=True)

## pandas를 이용한 시계열 자료로 변경 pandas.to_datetime(df['필드명'])

df1['사용일자'] = pd.to_datetime(df1['사용일자'])

# print(df1)
# print(df1.info())

df1['년'] = pd.to_datetime(df1['사용일자']).dt.year
df1['월'] = pd.to_datetime(df1['사용일자']).dt.month
df1['일'] = pd.to_datetime(df1['사용일자']).dt.day

cho = input('조회방법 선택 : \n1. 일자별 / 2. 월별\n')
st_name = input('조회할 역을 입력해주세요 : ')

if cho == '1':
    subway_sch2(df1, st_name)
elif cho == '2':
    subway_sch3(df1, st_name)

