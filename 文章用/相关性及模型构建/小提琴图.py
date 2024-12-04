import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

os.chdir(r"C:\Users\32766\Desktop")
data1 = pd.read_excel(r"C:\Users\32766\Desktop\性别比较.xlsx", header=0)

plt.style.use('ggplot')  # 使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'  # 设置背景颜色为白色
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为Times New Roman
my_pal_gender ={"Female": '#3199D3', "Male": '#4BAF71'}
# 创建图形
fig, ax = plt.subplots(figsize=(5, 4))
# 性别比较小提琴图
sns.violinplot(ax=ax, x=data1["Datasets"], y=data1["Residual"], bw_method=0.3, linewidth=1, width=0.7, alpha=1.0,
               palette=my_pal_gender, hue=None, scale='area', inner=None, saturation=0.9)
sns.boxplot(ax=ax, x=data1["Datasets"], y=data1["Residual"], data=data1, color="black", width=.10, zorder=10,
            showcaps=True, boxprops={'facecolor': 'none', "zorder": 10},
            showfliers=True, whiskerprops={'linewidth': 0.5, "zorder": 10},
            saturation=0.3, orient="v")
# 性别整体方差分析
group1 = data1[data1["Datasets"] == "Female"]["Residual"]
group2 = data1[data1["Datasets"] == "Male"]["Residual"]
t_stat, p_val = stats.ttest_ind(group1, group2)
if p_val < 0.05:
    ax.text(0.85, 0.96, f"p < 0.05", ha='center', fontweight='bold', fontsize=14, color='red', transform=ax.transAxes)
else:
    ax.text(0.25, 0.96, f"p = {p_val:.2f}", ha='center', fontweight='bold', fontsize=14, color='black', transform=ax.transAxes)
ax.set_ylabel("Absolute error (years)", fontweight='bold', color='black', fontsize=12)
ax.tick_params(axis='x', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.tick_params(axis='y', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.2)
ax.set_xlabel('')
plt.show()  # 显示图形
