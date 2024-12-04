
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.signal import savgol_filter

# 设置工作路径
os.chdir(r"C:\Users\32766\Desktop")

# 使用 ggplot 的绘图风格
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'  # 设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'  # 设置边框颜色为黑色
plt.rcParams['axes.grid'] = False  # 不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'  # 设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'  # 只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为 Times New Roman

# 读取数据
df = pd.read_excel(r"all_cpg_diff_sorted.xlsx", header=0)
total_mae = df['Difference'].to_numpy()  # 提取 'Difference' 列并转换为 numpy 数组

# 计算排名
ranking = np.argsort(np.argsort(-total_mae))  # 按照差值降序计算排名

# 获取差值最大的前100个点的索引
selected_indices = np.argsort(total_mae)[-100:]

# 创建与 total_mae 形状相同的全零数组，并将前100个差值最大的点赋给 selected_mae
selected_mae = np.zeros_like(total_mae)
selected_mae[selected_indices] = total_mae[selected_indices]
smoothed_mae = savgol_filter(total_mae, window_length=100, polyorder=90)
# 绘制图形
plt.figure(figsize=(6, 4))

# 填充所有数据区域
plt.fill_between(total_mae, ranking, color='#507CC4', alpha=1.0, label='All 300 Sites')

# 用红色填充前100个差值最大的点
plt.fill_between(total_mae[selected_indices], ranking[selected_indices], color='#D33E1B', alpha=1.0, label='Top 100 Sites')
plt.xlabel('Difference', fontweight='bold', color='black', fontsize=12)
plt.ylabel('Ranking', fontweight='bold', color='black', fontsize=12)

# 设置图形样式
ax = plt.gca()
ax.spines['top'].set_visible(False)  # 去除上框线
ax.spines['right'].set_visible(False)  # 去除右框线
ax.spines['bottom'].set_edgecolor('black')  # 自定义下框线
ax.spines['bottom'].set_linewidth(1.5)  # 自定义下框线
ax.spines['left'].set_edgecolor('black')  # 自定义左框线
ax.spines['left'].set_linewidth(1.5)  # 自定义左框线
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# 显示图例
plt.legend()

# 显示图形
plt.show()

