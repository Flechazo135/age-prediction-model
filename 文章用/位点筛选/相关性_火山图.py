import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import os
os.chdir(r"C:\Users\32766\Desktop")
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
df=pd.read_excel(r"cpg_correlation_results.xlsx", header=0)
# 假设df是你的数据表，包含'Pearson_Correlation'和'p-value'列
df['-log10(Pearson_p-value)'] = -np.log10(df['Pearson_p-value'])
# 自定义颜色：红色代表正相关大于等于0.7，蓝色代表负相关小于等于-0.7，其他为灰色
def assign_color(correlation):
    if correlation >= 0.7:
        return '#D33E1B'  # 红色
    elif correlation <= -0.7:
        return '#3B68B0'  # 蓝色
    else:
        return '#5d7092'  # 灰色
# 应用颜色分配函数
df['Color'] = df['Pearson_Correlation'].apply(assign_color)
# 绘制散点图
plt.figure(figsize=(6,6))
sns.scatterplot(
    x='Pearson_Correlation',
    y='-log10(Pearson_p-value)',
    data=df,
    c=df['Color'],  # 根据相关性值自定义颜色
    legend=False
)
# 添加阈值线：相关性绝对值为0.7，p值阈值为0.05
plt.axvline(x=0.7, color='black', linestyle='--', linewidth=1)
plt.axvline(x=-0.7, color='black', linestyle='--', linewidth=1)
plt.axhline(y=-np.log10(0.05), color='black', linestyle='--', linewidth=1)
# 添加标题和标签
plt.xlabel('Pearson Correlation',fontweight='bold',color='black',fontsize=12)
plt.ylabel('-log10(Pearson p-value)',fontweight='bold',color='black',fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)#去除上框线
ax.spines['right'].set_visible(False)#去除右框线
ax.spines['bottom'].set_edgecolor('black')#自定义下框线
ax.spines['bottom'].set_linewidth(1.5)#自定义下框线
ax.spines['left'].set_edgecolor('black')#自定义左框线
ax.spines['left'].set_linewidth(1.5)#自定义左框线
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.legend()
plt.show()