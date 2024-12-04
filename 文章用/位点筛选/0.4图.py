import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df = pd.read_excel(r"s1-B.xlsx", header=0)#读取数据
# 创建一个新的列，将ID映射为数值
df['ID'] = range(1, len(df) + 1)
# 设置颜色条件：大于0.4的为红色，其他为蓝色
colors = ['#D33E1B' if x > 0.4 else '#3B68B0' for x in df['差值']]
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
plt.figure(figsize=(6,6))
# 绘制散点图
plt.scatter(df['ID'], df['差值'], color=colors,s=12, alpha=0.8)
#添加虚线
plt.axhline(y=0.4, color='red',alpha=0.8, linestyle='--',linewidth=1.0)
for i, diff_value in enumerate(df['差值']):
    if diff_value == 0.400103993168446:
        # 添加对应的垂直线
        plt.axvline(x=df['ID'][i], color='red',alpha=0.8, linestyle='--',linewidth=1.0)
plt.xlabel('ID',fontweight='bold',color='black',fontsize=12)
plt.ylabel('Methylation Variation Range',fontweight='bold',color='black',fontsize=12)
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