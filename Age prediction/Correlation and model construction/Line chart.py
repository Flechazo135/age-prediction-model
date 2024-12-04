import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_excel(r"R2（diff bins）.xlsx", header=0)
bins = df['Bins']
RF  = df['RF']
DT = df['DT']
LDA = df['LDA']
ADB= df['ADB']
KNN = df['KNN']
LR= df['LR']
plt.figure(figsize=(8, 6))
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['font.family'] = 'Times New Roman'
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
# Each classifier uses different colors and symbols
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
plt.legend()
plt.show()
