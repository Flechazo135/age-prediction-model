import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df = pd.read_csv("GSE78874.csv",header=0)
# 打印原始数据
print("原始数据:")
print(df)
df_transposed = df.set_index('ID').transpose()
# 打印转换后的数据
print("\n行列转换后的数据:")
print(df_transposed)