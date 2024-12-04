import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
os.chdir(r"C:\Users\32766\Desktop")
data = pd.read_excel(r"C:\Users\32766\Desktop\Regional comparison.xlsx", header=0)
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.family'] = 'Times New Roman'
my_pal_gender = {
    "Australia": '#7150B4',
    "Caucasian-European": '#359787',
    "Caucasian-USA": '#E69F00',
    "Chinese": '#3C78BA',
    "Hispanic-European": '#2A87AC',
    "Hispanic-USA": '#C63D18',
    "Korean": '#EC7D0E',
}
fig, ax = plt.subplots(figsize=(10, 4))
sns.violinplot(ax=ax, x=data["Datasets"], y=data["Residual"], bw=0.3, linewidth=1, width=0.7, alpha=1.0,
               palette=my_pal_gender, hue=data["Datasets"], scale='area', inner=None, saturation=0.9)
sns.boxplot(ax=ax, x=data["Datasets"], y=data["Residual"], data=data, color="black", width=.10, zorder=10,
            showcaps=True, boxprops={'facecolor': 'none', "zorder": 10},
            showfliers=True, whiskerprops={'linewidth': 0.5, "zorder": 10},
            saturation=0.3, orient="v")
# Overall analysis of variance (ANOVA)
f_stat, p_val = stats.f_oneway(
    data[data["Datasets"] == "Australia"]["Residual"],
    data[data["Datasets"] == "Caucasian-European"]["Residual"],
    data[data["Datasets"] == "Caucasian-USA"]["Residual"],
    data[data["Datasets"] == "Chinese"]["Residual"],
    data[data["Datasets"] == "Hispanic-European"]["Residual"],
    data[data["Datasets"] == "Hispanic-USA"]["Residual"],
    data[data["Datasets"] == "Korean"]["Residual"]

)
# LSD post hoc test
tukey_result = pairwise_tukeyhsd(data['Residual'], data['Datasets'], alpha=0.05)
significance_levels = {}
for row in tukey_result.summary().data[1:]:
    group1 = row[0]
    group2 = row[1]
    reject = row[2]
    p_adj = row[3]
    if reject:
        if p_adj < 0.001:
            significance_levels[(group1, group2)] = '***'
        elif p_adj < 0.01:
            significance_levels[(group1, group2)] = '**'
        elif p_adj < 0.05:
            significance_levels[(group1, group2)] = '*'
groups_list = list(my_pal_gender.keys())
print(tukey_result)
print("Significance levels:", significance_levels)
# Add significance markers to the plot
def add_significance(ax, x1, x2, y, significance, offset=5):
    y_offset = offset
    line_color = 'black'
    line_width = 1.0
    ax.plot([x1, x1, x2, x2], [y, y + y_offset, y + y_offset, y], color=line_color, linewidth=line_width)
    significance_color = 'red'
    ax.text((x1 + x2) / 2, y + y_offset * 0.7, significance, ha='center', va='bottom', fontsize=20, color=significance_color)
def adjust_significance_positions(significance_levels, data, groups_list):
    y_offsets = {}
    offset_increment = 2
    for (group1, group2), significance in significance_levels.items():
        y = max(data[data["Datasets"].isin([group1, group2])]["Residual"])
        while any(abs(y - prev_y) < 0.5 for prev_y in y_offsets.values()):
            y += offset_increment
        y_offsets[(group1, group2)] = y
    return y_offsets
y_offsets = adjust_significance_positions(significance_levels, data, groups_list)
for (group1, group2), significance in significance_levels.items():
    y = y_offsets[(group1, group2)]
    add_significance(ax, groups_list.index(group1), groups_list.index(group2), y, significance, offset=5)
ax.set_ylabel("Absolute error (years)", fontweight='bold', color='black', fontsize=12)
ax.tick_params(axis='x', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.tick_params(axis='y', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.2)
ax.set_xlabel('')
plt.show()