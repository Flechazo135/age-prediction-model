import pandas as pd
from scipy.stats import pearsonr, spearmanr
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
#读取数据
data1 = pd.read_csv("GSE59509.csv", header=0)
data2 = pd.read_csv("GSE119078.csv", header=0)
data3 = pd.read_csv("GSE92767.csv", header=0)
data4 = pd.read_csv("GSE111223.csv", header=0)
data5 = pd.read_csv("GSE138279.csv", header=0)
data6 = pd.read_csv("GSE78874.csv", header=0)
#转置数据并设置索引
df1 = data1.set_index('ID').transpose()
df2 = data2.set_index('ID').transpose()
df3 = data3.set_index('ID').transpose()
df4 = data4.set_index('ID').transpose()
df5 = data5.set_index('ID').transpose()
df6 = data6.set_index('ID').transpose()
#获取共有的甲基化位点
common_cpgs = set(df1.columns)
for df in [df2, df3, df4, df5, df6]:
    common_cpgs = common_cpgs.intersection(set(df.columns))
print(f"共有的甲基化位点数量: {len(common_cpgs)}")
#提取共有甲基化位点的数据
df1_common = df1[list(common_cpgs)]
df2_common = df2[list(common_cpgs)]
df3_common = df3[list(common_cpgs)]
df4_common = df4[list(common_cpgs)]
df5_common = df5[list(common_cpgs)]
df6_common = df6[list(common_cpgs)]
#合并数据集
combined_df = pd.concat([df1_common, df2_common, df3_common, df4_common, df5_common, df6_common], axis=0)
print(combined_df)
#提取年龄数据
age = combined_df['age']
#计算Pearson和Spearman相关性
results = []
exclude_columns = ['age']  # 排除age列
for cpg_site in combined_df.columns:
    if cpg_site not in exclude_columns:
        pearson_corr, pearson_p = pearsonr(combined_df[cpg_site], age)
        spearman_corr, spearman_p = spearmanr(combined_df[cpg_site], age)
        results.append({
            'CpG_Site': cpg_site,
            'Pearson_Correlation': pearson_corr,
            'Pearson_p-value': pearson_p,
            'Spearman_Correlation': spearman_corr,
            'Spearman_p-value': spearman_p
        })
results_df = pd.DataFrame(results)#存储结果
filtered_results = results_df[results_df['Pearson_Correlation'].abs() >= 0.5]#筛选出pearson相关性绝对值大于等于0.7的位点
filtered_cpg_sites = filtered_results['CpG_Site'].tolist()#获取筛选后位点的列表
filtered_cpg_values = combined_df[['age'] + filtered_cpg_sites]#提取样本信息
results_df.to_excel('cpg_sites_values_with_age.xlsx')
filtered_cpg_values.to_excel('filtered_cpg_sites_values_with_age.xlsx', index=True)#输出所选cpg样本信息
filtered_results.to_excel('filtered_cpg_correlation_results.xlsx', index=False)#输出相关性筛选结果
print("筛选后的位点数据已保存到 'filtered_cpg_sites_values_with_age.xlsx'")
print("筛选后的相关性结果已保存到 'filtered_cpg_correlation_results.xlsx'")

