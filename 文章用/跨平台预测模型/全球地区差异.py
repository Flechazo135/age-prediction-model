import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 设置工作目录和数据
os.chdir(r"C:\Users\32766\Desktop")
data = pd.read_excel(r"C:\Users\32766\Desktop\地区比较-Dummy.xlsx", header=0)

plt.style.use('ggplot')  # 使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'  # 设置背景颜色为白色
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为Times New Roman
my_pal_gender = {
    "Australia": '#7150B4',
    "Caucasian-European": '#359787',
    "Caucasian-USA": '#E69F00',
    "Chinese": '#3C78BA',
    "Hispanic-European": '#2A87AC',
    "Hispanic-USA": '#C63D18',
    "Korean": '#EC7D0E',
}
# 创建图形
fig, ax = plt.subplots(figsize=(10, 4))
# 性别比较小提琴图
sns.violinplot(ax=ax, x=data["Datasets"], y=data["Residual"], bw=0.3, linewidth=1, width=0.7, alpha=1.0,
               palette=my_pal_gender, hue=data["Datasets"], scale='area', inner=None, saturation=0.9)
sns.boxplot(ax=ax, x=data["Datasets"], y=data["Residual"], data=data, color="black", width=.10, zorder=10,
            showcaps=True, boxprops={'facecolor': 'none', "zorder": 10},
            showfliers=True, whiskerprops={'linewidth': 0.5, "zorder": 10},
            saturation=0.3, orient="v")

#整体方差分析
f_stat, p_val = stats.f_oneway(
    data[data["Datasets"] == "Australia"]["Residual"],
    data[data["Datasets"] == "Caucasian-European"]["Residual"],
    data[data["Datasets"] == "Caucasian-USA"]["Residual"],
    data[data["Datasets"] == "Chinese"]["Residual"],
    data[data["Datasets"] == "Hispanic-European"]["Residual"],
    data[data["Datasets"] == "Hispanic-USA"]["Residual"],
    data[data["Datasets"] == "Korean"]["Residual"]

)


# LSD事后检验
tukey_result = pairwise_tukeyhsd(data['Residual'], data['Datasets'], alpha=0.05)

# 根据Tukey结果动态生成显著性标记字典
significance_levels = {}
for row in tukey_result.summary().data[1:]:  # 跳过第一行标题
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
# 将my_pal_gender的keys转换为列表以使用索引
groups_list = list(my_pal_gender.keys())

print(tukey_result)
print("Significance levels:", significance_levels)

# 在图中添加显著性标记
def add_significance(ax, x1, x2, y, significance, offset=5):
    y_offset = offset  # 线的高度偏移
    line_color = 'black'  # 自定义线条颜色
    line_width = 1.0  # 自定义线条粗细
    ax.plot([x1, x1, x2, x2], [y, y + y_offset, y + y_offset, y], color=line_color, linewidth=line_width)
    # 显著性标记的颜色
    significance_color = 'red'  # 自定义显著性标记颜色
    ax.text((x1 + x2) / 2, y + y_offset * 0.7, significance, ha='center', va='bottom', fontsize=20, color=significance_color)
# 动态设置显著性标记的 y 位置
def adjust_significance_positions(significance_levels, data, groups_list):
    y_offsets = {}  # 用来存储每对组间差异的y偏移量
    offset_increment = 2  # 每次偏移的增加量

    # 遍历显著性结果并为每个比较设置偏移量
    for (group1, group2), significance in significance_levels.items():
        y = max(data[data["Datasets"].isin([group1, group2])]["Residual"])  # 找到最大值作为y坐标

        # 确保y_offset不与其他显著性标记重合
        while any(abs(y - prev_y) < 0.5 for prev_y in y_offsets.values()):
            y += offset_increment  # 增加偏移量，避免重叠

        y_offsets[(group1, group2)] = y  # 记录新的y位置

    return y_offsets


# 获取显著性标记位置
y_offsets = adjust_significance_positions(significance_levels, data, groups_list)

# 将显著性标记添加到图中
for (group1, group2), significance in significance_levels.items():
    y = y_offsets[(group1, group2)]  # 获取调整后的y位置
    add_significance(ax, groups_list.index(group1), groups_list.index(group2), y, significance, offset=5)

# 设置坐标轴标签
ax.set_ylabel("Absolute error (years)", fontweight='bold', color='black', fontsize=12)
ax.tick_params(axis='x', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.tick_params(axis='y', labelsize=10, labelrotation=0, direction='out', length=6, width=2, colors='black')
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.2)
ax.set_xlabel('')
plt.show()  # 显示图形

