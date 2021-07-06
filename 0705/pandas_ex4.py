import pandas as pd

df1 = pd.read_csv("./multi/0705/data/서울시CCTV.csv", encoding='cp949')

# print(df1)

df1 = df1.dropna(how='all')
print(df1)