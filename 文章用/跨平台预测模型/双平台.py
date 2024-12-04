import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import os

# 设置工作目录
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_excel(r"C:\Users\32766\Desktop\450k+283全部-1_prediction_results.xlsx", header=0)

# 定义X和y
X = df['age']
y = df['Predicted_Age']
dummy = df['Dummy']

# 计算R²和MAE
r2 = r2_score(X, y)
mae = mean_absolute_error(X, y)

# 使用ggplot的绘图风格
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(5,5))

# 按照Dummy值绘制不同颜色和标记的散点图
plt.scatter(X[dummy == 0], y[dummy == 0], color='#1B78AB', alpha=1.0, s=35, label='SNaPshot', marker='D')
plt.scatter(X[dummy == 1], y[dummy == 1], color='#e8684a', alpha=1.0, s=35, label='Illumina 450K', marker='o')

# 绘制参考线
plt.plot([min(X), max(X)], [min(y), max(y)], linestyle='--', color='#000000', linewidth=1.0, alpha=1.0)

# 设置坐标轴标签
plt.xlabel('Chronological Age (years)', fontweight='bold', color='black', fontsize=12)
plt.ylabel('Predicted Age (years)', fontweight='bold', color='black', fontsize=12)

# 显示R²和MAE
plt.text(0.7, 0.05, f"R² = {r2 * 100:.2f}%\nMAE = {mae:.2f}", transform=plt.gca().transAxes, color='black', fontsize=12)

# 美化图形2
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

# 添加图例
plt.legend()
plt.show()
