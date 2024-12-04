import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roma
os.chdir(r"C:\Users\32766\Desktop")#设置路径
file_path = '不同年龄段比较-fig5B.xlsx'
data= pd.read_excel(file_path)
data.set_index("Models", inplace=True)
colors = ['#7150B4','#2A87AC','#359787','#E69F00','#EC7D0E','#C63D18']
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)
plt.figure(figsize=(4, 6))
sns.heatmap(data, annot=True, fmt=".4f", cmap=custom_cmap)
ax = plt.gca()
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
# 设置坐标轴刻度标签颜色为黑色
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.spines['top'].set_visible(False)#去除上框线
ax.spines['right'].set_visible(False)#去除右框线
ax.set_ylabel('')
plt.show()

import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

plt.style.use('ggplot')  # 使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'  # 设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'  # 设置边框颜色为黑色
plt.rcParams['axes.grid'] = False  # 不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'  # 设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'  # 只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为Times New Roman

os.chdir(r"C:\Users\32766\Desktop")  # 设置路径
file_path = '不同年龄段比较-fig5B.xlsx'
data = pd.read_excel(file_path)
data.set_index("Models", inplace=True)

# 按均值排序行
data_sorted = data.loc[data.mean(axis=1).sort_values().index]

colors = ['#7150B4', '#2A87AC', '#359787', '#E69F00', '#EC7D0E', '#C63D18']
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

plt.figure(figsize=(5, 6))
sns.heatmap(data_sorted, annot=True, fmt=".2f", cmap=custom_cmap)

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
ax.set_ylabel('')

plt.show()

