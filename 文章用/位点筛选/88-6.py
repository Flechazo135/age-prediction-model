import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
df = pd.read_excel("top_300_cpg_filtered_with_id_age.xlsx")

# 获取6岁和88岁的样本数据
age_6_samples = df[df['age'] == 6].iloc[:, 2:].mean()
age_88_samples = df[df['age'] == 88].iloc[:, 2:].mean()

# 计算每个cg点的差值（绝对值）
diff = (age_88_samples - age_6_samples).abs()

# 筛选出绝对值差值最大的100个位点
top_100_cpgs = diff.nlargest(100)

# 提取这些位点对应的所有样本数据
top_100_cpgs_data = df[['ID', 'age'] + top_100_cpgs.index.tolist()]

# 保存到新的Excel文件
output_file_path = 'top_100_cpg_diff.xlsx'
top_100_cpgs_data.to_excel(output_file_path, index=False)
# 按照差值绝对值从大到小排列所有位点
all_cpg_diff = pd.DataFrame({
    'CpG_site': diff.index,
    'Difference': diff.values
}).sort_values(by='Difference', ascending=False)

# 保存到新的Excel文件
output_all_diff_file_path = 'all_cpg_diff_sorted.xlsx'
all_cpg_diff.to_excel(output_all_diff_file_path, index=False)

output_all_diff_file_path




