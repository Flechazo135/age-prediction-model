import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")
df=pd.read_excel("GSE59509.xlsx",header=0)
rows_with_na = df[df.isna().any(axis=1)].index.tolist()
df_cleaned = df.dropna(axis=0)
df_cleaned.to_csv('GSE59509.csv', index=False)