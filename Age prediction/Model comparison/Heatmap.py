import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['font.family'] = 'Times New Roman'
os.chdir(r"C:\Users\32766\Desktop")
file_path = 'fig5B.xlsx'
data = pd.read_excel(file_path)
data.set_index("Models", inplace=True)
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
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylabel('')
plt.show()

