import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
os.chdir(r"C:\Users\32766\Desktop")
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
df=pd.read_excel(r"300互信息55.xlsx", header=0)
all_mutual_info = df['MI Score'].to_numpy()  # 将Series转换为numpy数组
selected_indices = np.argsort(all_mutual_info)[-100:]  # 获取排序后的前100个索引
selected_mutual_info = np.zeros_like(all_mutual_info)  # 创建一个与all_mutual_info形状相同的全零数组
selected_mutual_info[selected_indices] = all_mutual_info[selected_indices]
plt.figure(figsize=(6, 4))
plt.fill_between(range(len(all_mutual_info)), all_mutual_info, color='#3B68B0',alpha=1.0, label='All 2448 Sites')
plt.fill_between(selected_indices, all_mutual_info[selected_indices], color='#D33E1B', alpha=1.0, label='Top 300 Sites')
plt.xlabel('Feature Index',fontweight='bold',color='black',fontsize=12)
plt.ylabel('Mutual Information Score',fontweight='bold',color='black',fontsize=12)
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