import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir(r"C:\Users\32766\Desktop")#设置路径
data =pd.read_excel(r"C:\Users\32766\Desktop\模型比较.xlsx", header=0)#读取数据

# 第二步：绘制带有性别分类的抖动散点图
plt.figure(figsize=(10, 6))
# 自定义颜色
custom_palette = 'Set2'  # 或者你可以定义自己的调色板

# 绘制抖动散点图，使用自定义颜色、大小、透明度
sns.stripplot(x='Model', y='MAE', data=data, jitter=True, palette=custom_palette,
              size=8, alpha=0.6)

# 叠加每个模型的平均值 (使用pointplot添加平均值线)
sns.pointplot(x='Model', y='MAE', data=data, palette=custom_palette,
              markers='D', linestyles='', scale=1.2, ci=None, join=False)
plt.xlabel('Models', fontsize=12)
plt.ylabel('MAE', fontsize=12)

# 添加图例
plt.legend(title='Gender')

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.show()
