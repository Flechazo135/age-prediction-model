import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy import stats

plt.style.use('ggplot')  # 使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'  # 设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'  # 设置边框颜色为黑色
plt.rcParams['axes.grid'] = False  # 不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'  # 设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'  # 只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为Times New Roman

os.chdir(r"C:\Users\32766\Desktop")  # 设置路径
file_path = '模型比较.xlsx'
data_df = pd.read_excel(file_path)

# 计算均值和标准误差（SEM）
grouped_data = data_df.groupby('Models')['Absolute error'].agg(['mean', 'sem']).reset_index()

# 按均值对数据进行排序
grouped_data = grouped_data.sort_values(by='mean', ascending=True)  # 按均值升序排序

# 提取组别名称、均值和标准误差
categories = grouped_data['Models'].tolist()
means = grouped_data['mean'].tolist()
std_errors = grouped_data['sem'].tolist()

bar_colors = ['#7150B4', '#3C78BA', '#2A87AC', '#359787', '#E69F00', '#EC7D0E', '#C63D18']
error_colors = ['#6748A6', '#267C9E', '#318B7C', '#2F8577', '#DA9700', '#D9730D', '#B93A17']

fig, ax = plt.subplots(figsize=(8, 6))
bars = []  # 用于存储条形对象

for i, (category, mean, std_err, bar_color, err_color) in enumerate(zip(categories, means, std_errors, bar_colors, error_colors)):
    bar = ax.bar(category, mean, yerr=std_err, capsize=10, color=bar_color, alpha=0.7, edgecolor=bar_color,
                  error_kw={'ecolor': err_color, 'elinewidth': 1.8})
    bars.append(bar)

ax.scatter(categories, means, color='red', alpha=0.7, marker='o', s=75, label='Mean')
ax.set_ylabel('Absolute error (years)', color='black', fontsize=12)

ax = plt.gca()
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')

# 设置坐标轴刻度标签颜色为黑色
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.spines['top'].set_visible(False)  # 去除上框线
ax.spines['right'].set_visible(False)  # 去除右框线

plt.show()
