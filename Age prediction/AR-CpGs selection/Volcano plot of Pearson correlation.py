import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
os.chdir(r"C:\Users\32766\Desktop")
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['font.family'] = 'Times New Roman'
df=pd.read_excel(r"cpg_correlation_results.xlsx", header=0)
df['-log10(Pearson_p-value)'] = -np.log10(df['Pearson_p-value'])
def assign_color(correlation):
    if correlation >= 0.7:
        return '#D33E1B'
    elif correlation <= -0.7:
        return '#3B68B0'
    else:
        return '#5d7092'
df['Color'] = df['Pearson_Correlation'].apply(assign_color)
plt.figure(figsize=(6,6))
sns.scatterplot(
    x='Pearson_Correlation',
    y='-log10(Pearson_p-value)',
    data=df,
    c=df['Color'],
    legend=False
)
plt.axvline(x=0.7, color='black', linestyle='--', linewidth=1)
plt.axvline(x=-0.7, color='black', linestyle='--', linewidth=1)
plt.axhline(y=-np.log10(0.05), color='black', linestyle='--', linewidth=1)
plt.xlabel('Pearson Correlation',fontweight='bold',color='black',fontsize=12)
plt.ylabel('-log10(Pearson p-value)',fontweight='bold',color='black',fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.legend()
plt.show()