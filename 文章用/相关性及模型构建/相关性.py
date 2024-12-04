import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import pearsonr, spearmanr
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df = pd.read_excel(r"C:\Users\32766\Desktop\283终.xlsx", header=0)#读取数据
columns = ['cg07547549','cg00481951','cg21296230', 'cg10501210', 'cg13654588',
           'cg14361627', 'cg17885226', 'cg17110586', 'cg15480367', 'cg19671120']
y = 'age'
x_min = df[columns].min().min()
x_max = df[columns].max().max()
y_min = df[y].min() - 7
y_max = df[y].max() + 9
#绘图
plt.style.use('ggplot')#使用ggplot的绘图风格
plt.rcParams['axes.facecolor'] = 'white'#设置背景颜色为白色
plt.rcParams['axes.edgecolor'] = 'black'#设置边框颜色为黑色
plt.rcParams['axes.grid'] = False#不显示网格线
plt.rcParams['axes.grid.axis'] = 'both'#设置网格线显示在坐标轴两侧
plt.rcParams['axes.grid.which'] = 'major'#只显示主要网格线
plt.rcParams['font.family'] = 'Times New Roman'#设置字体为Times New Roman
#10个子图
#colors = ['#589FF3', '#589FF3', '#589FF3','#589FF3','#589FF3', '#F38169', '#F39169','#F38169','#F94141', '#37AB78']#定义颜色
colors = ['#1C7FB6','#1C7FB6','#1C7FB6','#1C7FB6','#1C7FB6',
          '#E76C07','#E76C07','#E76C07','#E76C07','#E76C07']
#colors =['#7fb8dd','#9ccc65','#5d7092','#ffb300','#e8684a','#81c784','#7988d2','#ff9d4d','#5b8ff9','#ff99c3'（粉）]#定义颜色(第一版）
fig, axs = plt.subplots(2, 5, figsize=(20, 10)) #2行5列的子图网格
for i, col in enumerate(columns):
    ax = axs[i // 5, i % 5]
    sns.regplot(x=df[col], y=y, data=df, ax=ax, color=colors[i], scatter_kws={'s': 10, 'alpha': 0.8},
                line_kws={'linewidth': 1.5, 'alpha': 0.7}, label=None)
    corr, p_value = pearsonr(df[col], df[y]) #计算pearsonr相关性和p值
    label = f'{col} \n(r={corr:.2f} p={p_value:.2e})'#生成标签，包含相关系数和p值，使用科学记数法显示p值
    x_min = df[col].min()-0.02
    x_max = df[col].max()+0.02
    y_min = df[y].min()-4
    y_max = df[y].max()+4
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel('DNAm', fontsize=10,color='black', fontweight='bold')
    ax.set_ylabel('Age (years)', fontsize=10,color='black', fontweight='bold')
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    # 设置坐标轴刻度标签颜色为黑色
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')
    if i == 0:
        ax.text(0.97, 0.95, label, ha='right', va='top', transform=ax.transAxes, fontsize=8, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    else:
        ax.text(0.965, 0.95, label, ha='right', va='top', transform=ax.transAxes, fontsize=8, fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    ax.tick_params(axis='both', which='both', direction='in', bottom=True, top=False, left=True, right=False)
    #绘制自变量的边际拟合线轴
    x_marginal_ax = ax.inset_axes([0, 1.0, 1, 0.2], sharex=ax)
    sns.kdeplot(df[col], ax=x_marginal_ax, color=colors[i], linewidth=1, fill=True, alpha=0.8)
    x_marginal_ax.set_yticks([])
    x_marginal_ax.xaxis.set_visible(False)
    x_marginal_ax.set_xlabel('')
    x_marginal_ax.set_ylabel('')
    x_marginal_ax.spines['top'].set_visible(False)
    x_marginal_ax.spines['right'].set_visible(False)
    x_marginal_ax.spines['left'].set_visible(False)
    x_marginal_ax.spines['bottom'].set_visible(False)
    x_marginal_ax.tick_params(axis='both', which='both', direction='in', bottom=True, top=False, left=True, right=False)
    #添加y轴边际拟合线轴
    if i == 4 or i == 9:
        y_marginal_ax = ax.inset_axes([1.0, 0, 0.2, 1], sharey=ax)
        sns.kdeplot(df[y], ax=y_marginal_ax, color='#949494', linewidth=1, vertical=True, fill=True, alpha=0.8)
        y_marginal_ax.set_xticks([])
        y_marginal_ax.yaxis.set_visible(False)
        y_marginal_ax.set_xlabel('')
        y_marginal_ax.set_ylabel('')
        y_marginal_ax.spines['top'].set_visible(False)
        y_marginal_ax.spines['right'].set_visible(False)
        y_marginal_ax.spines['left'].set_visible(False)
        y_marginal_ax.spines['bottom'].set_visible(False)
        y_marginal_ax.tick_params(axis='both', which='both', direction='in', bottom=True, top=False, left=True,
                                  right=False)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()