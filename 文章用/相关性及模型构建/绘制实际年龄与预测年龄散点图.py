import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import os
os.chdir(r"C:\Users\32766\Desktop")
df=pd.read_excel(r"C:\Users\32766\Desktop\283_RFC_bins=30_prediction_results.xlsx",header=0)
X=df['age']
y=df['Predicted_Age']
r2 = r2_score(X, y)
mae = mean_absolute_error(X, y)
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='#1B78AB', alpha=0.9, s=70)
plt.plot([min(X), max(X)], [min(y), max(y)], linestyle='--', color='#F8750E',linewidth=1.0,alpha=1.0)
plt.xlabel('Chronological Age (years)',fontweight='bold',color='black',fontsize=12)
plt.ylabel('Predicted Age (years)',fontweight='bold',color='black',fontsize=12)
#plt.title('Ensemble Model-Results',fontweight='bold',fontsize=16,pad=40)
plt.text(0.1, 0.9, f"R² = {r2 * 100:.2f}%\nMAE = {mae:.2f}", transform=plt.gca().transAxes,color='black',fontsize=14)
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