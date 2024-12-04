import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import os
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_excel("2448.xlsx")
X = df.drop(columns=['ID', 'age'])
y = df['age']
# 计算互信息
mi_scores = mutual_info_regression(X, y, discrete_features=False,n_neighbors=55,random_state=123)
# 将特征和对应的互信息得分转为DataFrame
mi_df = pd.DataFrame({'Feature': X.columns, 'MI Score': mi_scores})
# 按照互信息得分从高到低排序，取前100个CpG位点
top_300_features = mi_df.sort_values(by='MI Score', ascending=False).head(300)
# 提取这100个CpG位点的原始数据，同时纳入 'age' 和 'ID'
top_300_cpg_data = df[['ID', 'age'] + list(top_300_features['Feature'])]
# 将筛选后的前100个CpG位点及其原始信息（包括age和ID）保存到新的Excel文件
top_300_cpg_data.to_excel('top_300_cpg_filtered_with_id_age.xlsx', index=False)
print("经过互信息筛选的前100个CpG位点及其ID和年龄信息已保存到 'top_300_cpg_filtered_with_id_age.xlsx'")
# 转换成DataFrame以便查看
mi_df = pd.DataFrame({'Feature': X.columns, 'MI Score': mi_scores})
mi_df = mi_df.sort_values(by='MI Score', ascending=False)
print(mi_df)
# 将结果转换为 DataFrame
mi_df = pd.DataFrame(mi_df).sort_values(by='MI Score', ascending=False)
# 保存到 Excel 文件
mi_df.to_excel('300互信息55.xlsx', index=False)