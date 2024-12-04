import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import os
os.chdir(r"C:\Users\32766\Desktop")
df=pd.read_excel(r"283_RFC_bins=30_prediction_results.xlsx",header=0)
X=df['age']
y=df['Predicted_Age']
r2 = r2_score(X, y)
mae = mean_absolute_error(X, y)
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='#1B78AB', alpha=0.9, s=70)
plt.plot([min(X), max(X)], [min(y), max(y)], linestyle='--', color='#F8750E',linewidth=1.0,alpha=1.0)
plt.xlabel('Chronological Age (years)',fontweight='bold',color='black',fontsize=12)
plt.ylabel('Predicted Age (years)',fontweight='bold',color='black',fontsize=12)
plt.text(0.1, 0.9, f"R² = {r2 * 100:.2f}%\nMAE = {mae:.2f}", transform=plt.gca().transAxes,color='black',fontsize=14)
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