import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
os.chdir(r"C:\Users\32766\Desktop")
data = pd.read_excel(r"C:\Users\32766\Desktop\RF.xlsx", header=0)
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'Times New Roman'
my_pal_gender = {"bins = 10":'#376EAB', "bins = 15":'#318B7C',"bins = 20":'#D9730D',
                 "bins = 25":'#6748A6',"bins = 30":'#DA9700',"bins = 35": '#267C9E'}
fig, ax = plt.subplots(figsize=(9,4))
# Violin plot
sns.violinplot(ax=ax, x=data["bins"], y=data["error"], bw_method=0.3, linewidth=1, width=0.7, alpha=1.0,
               palette=my_pal_gender, hue=None, scale='area', inner=None, saturation=0.9)
# Boxplot
sns.boxplot(ax=ax, x=data["bins"], y=data["error"], color="black", width=.10, zorder=10,
            showcaps=True, boxprops={'facecolor': 'none', "zorder": 10},
            showfliers=True, whiskerprops={'linewidth': 0.5, "zorder": 10},
            saturation=0.3, orient="v")
# Overall variance analysis
group1 = data[data["bins"] == "bins = 10"]["error"]
group2 = data[data["bins"] == "bins = 15"]["error"]
group3 = data[data["bins"] == "bins = 20"]["error"]
group4 = data[data["bins"] == "bins = 25"]["error"]
group5 = data[data["bins"] == "bins = 30"]["error"]
group6 = data[data["bins"] == "bins = 35"]["error"]
f_stat, p_val = stats.f_oneway(group1, group2, group3, group4, group5, group6 )
if p_val < 0.05:
    ax.text(0.1, 0.98, f"p < 0.05", ha='center', fontweight='bold', fontsize=14, color='red', transform=ax.transAxes)
else:
    ax.text(0.1, 0.98, f"p = {p_val:.2f}", ha='center', fontweight='bold', fontsize=14, color='black', transform=ax.transAxes)
ax.set_ylabel("Absolute error (years)", fontweight='bold', color='black', fontsize=12)
ax.tick_params(axis='x', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.tick_params(axis='y', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.2)
ax.set_xlabel('')
ax.set_title('RF')
plt.show()