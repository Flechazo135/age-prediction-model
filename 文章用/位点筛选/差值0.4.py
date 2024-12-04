
import pandas as pd
import os
os.chdir(r"C:\Users\32766\Desktop")
df = pd.read_excel("filtered_cpg_sites_values_with_age0.7.xlsx")
df = df.drop(columns=["ID"])
# 计算每列的最大值和最小值
max_values_per_column = df.max(axis=0)
min_values_per_column = df.min(axis=0)

# 计算最大值与最小值的差值
diff_values_per_column = max_values_per_column - min_values_per_column

# 创建一个新的DataFrame，存储差值
diff_df = pd.DataFrame({'最大值': max_values_per_column,
                        '最小值': min_values_per_column,
                        '差值': diff_values_per_column})

# 保存差值到 Excel 文件
diff_df.to_excel('STEP1：2448.xlsx', sheet_name='差值')

# 筛选出差值大于 0.4 的列
filtered_columns = df.loc[:, diff_values_per_column > 0.4]

# 保存筛选后的数据到 Excel 文件中的一个新工作表
with pd.ExcelWriter('STEP1：2448.xlsx', mode='a') as writer:
    filtered_columns.to_excel(writer, sheet_name='差值大于0.4的列')

print("差值和筛选结果已保存")