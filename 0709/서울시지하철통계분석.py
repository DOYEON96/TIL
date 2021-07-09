# import sys
# sys.path.append('./multi/0708/')
import pandas as pd
from tqdm import tqdm

# import mission
# import 

# - 각 파일에서 추가되지 않은 데이터를 api를 이용해 가져와 추가하기
# - 승하차 데이터 유/무임 승하차 데이터를 이용해 년도별 월별 데이터 생성
# - 역 입력시 해당 역의 승/하차, 유/무임 데이터 확인 및 시각화
# - 유/무임 승하차가 가장 많은 역 확인


df0 = pd.read_csv('./multi/0709/data/seoul_sw_inout.csv')
df1 = pd.read_csv('./multi/0709/data/seoul_sw_payfree.csv')

# # 두 데이터 프레임 모두 사용일/사용월 데이터 타입을 str형태로 변경
df0 = df0.astype({'사용일':str})

df1 = df1.astype({'사용일':str})
df1.columns = ['사용년월', '라인', '역명', '유임승차', '무임승차', '유임하차', '무임하차']
# print(df1.head())
    
df0['사용년월'] = df0['사용일'].str[:-2]
# print(df0.tail())

# print(df0.info())
df2 = df0.groupby(['사용년월', '라인', '역명']).sum()
df2 = df2.reset_index()
# print(df2)

# df3 = pd.concat([df1, df2], axis = 1)
# print(df1.info())
# print(df2.info())

df4 = pd.merge(df1, df2, on=['사용년월', '라인', '역명'], how = 'outer')

print(df4)

# df4 = pd.concat([df2, df3], axis=0, join='outer')

# print(df4)


# print(df1.iloc[0,0])
# df1['승차'] = ''
# df1['하차'] = ''

# for i in tqdm(range(len(df1))):
#     for j in range(len(df2)):
#         if (df1.iloc[i,0]==df2.iloc[j,0]) & (df1.iloc[i,1]==df2.iloc[j,1]) & (df1.iloc[i,2]==df2.iloc[j,2]):
#             df1.iloc[i,7] = df2.iloc[j, 3]
#             df1.iloc[i,8] = df2.iloc[j, 4]
#             print(df1.iloc[i,:])
#             break
# print(df1)
# print(df1)

# print(df1.info())
# print(df2.info())


# df4 = df4.reset_index()
# print(df4)

