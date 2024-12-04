import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df=pd.read_excel("GSE59509.xlsx",header=0)#读取数据集
rows_with_na = df[df.isna().any(axis=1)].index.tolist()#找到含缺失值的行的索引
df_cleaned = df.dropna(axis=0)#去除含缺失值的行
df_cleaned.to_csv('GSE59509.csv', index=False)#保存数据集