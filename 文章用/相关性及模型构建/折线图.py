import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df = pd.read_excel(r"折线图R2（不同分类器不同bins）.xlsx", header=0)#读取数据
bins = df['Bins']
RF  = df['RF']
DT = df['DT']
LDA = df['LDA']
ADB= df['ADB']
KNN = df['KNN']
LR= df['LR']
plt.figure(figsize=(8, 6))
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
ax = plt.gca()
ax.spines['top'].set_visible(False)#去除上框线
ax.spines['right'].set_visible(False)#去除右框线
ax.spines['bottom'].set_edgecolor('black')#自定义下框线
ax.spines['bottom'].set_linewidth(1.5)#自定义下框线
ax.spines['left'].set_edgecolor('black')#自定义左框线
ax.spines['left'].set_linewidth(1.5)#自定义左框线
#每个分类器使用不同的颜色和符号
plt.plot(bins, ADB, marker='D', color='#6748A6', label='ADB', markersize=10, linewidth=2, alpha=1.0)
plt.plot(bins, DT, marker='s', color='#318B7C', label='DT', markersize=10, linewidth=2, alpha=1.0)
plt.plot(bins, KNN, marker='v', color='#DA9700', label='KNN', markersize=10, linewidth=2, alpha=1.0)
plt.plot(bins, LDA, marker='*', color='#D9730D', label='LDA', markersize=10, linewidth=2, alpha=1.0)
plt.plot(bins, LR, marker='o', color='#267C9E', label='LR', markersize=10, linewidth=2, alpha=1.0)
plt.plot(bins, RF, marker='^', color='#376EAB', label='RF', markersize=10, linewidth=2, alpha=1.0)
ax.set_xlabel('Bins (years)', fontsize=12, color='black', fontweight='bold')
ax.set_ylabel('R²', fontsize=12, color='black', fontweight='bold')
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.legend()# 显示图例
plt.show()
