from statistics import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import SVR
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
from sklearn.model_selection import KFold
import os
os.chdir(r"C:\Users\32766\Desktop")#设置路径
data = pd.read_excel(r"C:\Users\32766\Desktop\450k+283全部-1.xlsx", header=0)#读取数据
X = data.drop(['age', 'ID','gender','ethnicity'], axis=1)#确定数据X
y = data['age']#确定数据y
IDs = data['ID']
repeats = 5#100次
cv_folds = 10#十折交叉验证
all_fold_mae_results = []#用于存储每次外层循环中每一折的MAE结果
all_fold_r2_results = []#用于存储每次外层循环中每一折的R2结果
mean_mae_results = []#用于存储每次外层循环的平均MAE值
mean_r2_results = []#用于存储每次外层循环的平均R2值
predicted_ages = np.zeros((len(y), repeats))#创建二维数组，每一行表示一个样本，数组的每一列表示一个重复实验
for iteration in range(repeats):
    kf = KFold(n_splits=cv_folds, shuffle=True)
    fold_mae = []#存储每次交叉验证的MAE值
    fold_r2 = []#存储每次交叉验证的R2值
    #交叉验证
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        ID_test = IDs.iloc[test_index]
        model = RandomForestRegressor()
        # AdaBoostRegressor()
        # XGBRegressor()
        # Ridge()
        # SVR(kernel='rbf')#kernel='poly',kernel='linear',kernel='sigmoid',kernel='rbf'
        # RandomForestRegressor()
        # LinearRegression()
        model = model.fit(X_train, y_train)  # 拟合模型
        y_pred = model.predict(X_test)  # 预测
        mae = mean_absolute_error(y_test, y_pred)#计算当前折的MAE
        r2 = r2_score(y_test, y_pred)#计算当前折的R2
        fold_mae.append(mae)#存储到相应的存储表格
        fold_r2.append(r2)#存储到相应的存储表格
        for idx, pred_age in zip(test_index, y_pred):
            predicted_ages[idx, iteration] = pred_age
    all_fold_mae_results.append(fold_mae)#存储当前外层循环中每一折的结果
    all_fold_r2_results.append(fold_r2)#存储当前外层循环中每一折的结果
    mean_mae = np.mean(fold_mae)#计算当前重复实验的平均MAE
    mean_r2 = np.mean(fold_r2)#计算当前重复实验的平均R2
    mean_mae_results.append(mean_mae)#存储平均MAD
    mean_r2_results.append(mean_r2)#存储平均R2
overall_mean_mae = np.mean(mean_mae_results)#计算100次循环的总体平均MAD
overall_mean_r2 = np.mean(mean_r2_results)#计算100次循环的总体平均R2
#输出预测结果
average_predicted_ages = np.mean(predicted_ages, axis=1)#计算100次循环的平均预测年龄
output_data = data[['ID'] + list(X.columns) + ['age']].copy()
output_data['Predicted_Age'] = average_predicted_ages#创建包含ID，10个CpG值，实际年龄，预测年龄的DataFrame
output_file_path_predictions = r"C:\Users\32766\Desktop\RFR-831_prediction_results.xlsx"
output_data.to_excel(output_file_path_predictions, index=False)
print(f"预测年龄结果已输出到Excel文件: {output_file_path_predictions}")