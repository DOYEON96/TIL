import pandas as pd

df1=pd.read_csv('./multi/0705/data/report.txt', sep ='\t', header=1)

df1 = df1.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]]

df1.drop(0, inplace = True)

col_name = ['년도', '자치구', '총인구', '총인구(남)', '총인구(여)', '내국인', '내국인(남)', '내국인(여)', '외국인', '외국인(남)', '외국인(여)', '65세이상']

df1.columns = col_name

# print(df1)

df2 = df1.iloc[:, [0, 1, 2, 5, 8, 11]]

# print(df2.dtypes)

# for row_i in df.index:
#     df.loc[row_i, "총인구"]=df2.loc[row_i, "총인구"].replace(',','')
#     df.loc[row_i, "내국인"]=df2.loc[row_i, "내국인"].replace(',','')
#     df.loc[row_i, "외국인"]=df2.loc[row_i, "외국인"].replace(',','')
#     df.loc[row_i, "65세이상"]=df2.loc[row_i, "65세이상"].replace(',','')


for i in range(2, len(df2.columns)):
    df2.iloc[:,i] = df2.iloc[:,i].str.replace(',','')

df2 = df2[df2['내국인'] != '…']

df2 = df2.astype({'총인구':int, '내국인':int, '외국인':int, '65세이상':int})

print(df2)