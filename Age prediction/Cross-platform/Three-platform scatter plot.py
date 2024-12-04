import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import os
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_excel(r"C:\Users\32766\Desktop\three with dummy_prediction_results.xlsx", header=0)
X = df['age']
y = df['Predicted_Age']
dummy_1 = df['Dummy_1']
dummy_2 = df['Dummy_2']
r2 = r2_score(X, y)
mae = mean_absolute_error(X, y)
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(5, 5))
plt.scatter(X[(dummy_1 == 0) & (dummy_2 == 0)], y[(dummy_1 == 0) & (dummy_2 == 0)],
            color='#1775AA', alpha=1.0, s=20, label='SNaPshot', marker='D')
plt.scatter(X[(dummy_1 == 1) & (dummy_2 == 0)], y[(dummy_1 == 1) & (dummy_2 == 0)],
            color='#FF7C00', alpha=1.0, s=37, label='MPS', marker='^')
plt.scatter(X[(dummy_1 == 0) & (dummy_2 == 1)], y[(dummy_1 == 0) & (dummy_2 == 1)],
            color='#5F4B8B', alpha=1.0, s=15, label='Illumina 450K', marker='o')
plt.plot([min(X), max(X)], [min(y), max(y)], linestyle='--', color='#000000', linewidth=1.0, alpha=1.0)
plt.xlabel('Chronological Age (years)', fontweight='bold', color='black', fontsize=12)
plt.ylabel('Predicted Age (years)', fontweight='bold', color='black', fontsize=12)
plt.text(0.7, 0.05, f"R² = {r2 * 100:.2f}%\nMAE = {mae:.2f}", transform=plt.gca().transAxes, color='black', fontsize=12)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.legend()
plt.show()