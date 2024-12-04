import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_csv("GSE78874.csv",header=0)
print("Raw data:")
print(df)
df_transposed = df.set_index('ID').transpose()
print("\nTransformed data:")
print(df_transposed)