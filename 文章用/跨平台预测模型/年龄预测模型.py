import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np
from sklearn.model_selection import KFold
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
os.chdir(r"C:\Users\32766\Desktop")#设置路径
data = pd.read_excel(r"C:\Users\32766\Desktop\0924.xlsx", header=0)#读取数据
#X = data.drop(['age', 'ID','gender','ethnicity'], axis=1)#确定数据X
X = data.drop(['age', 'ID','Dummy_1','Dummy_2'], axis=1)#确定数据X
y = data['age']#确定数据y
IDs = data['ID']
repeats = 5#5次
cv_folds = 10#十折交叉验证
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
        #定义年龄组函数
        def age_groups(y, groups):
            bins = np.concatenate(([1], groups, [91]))
            return np.digitize(y, bins)-1
        #存储所有分类器
        classifiers = []
         #训练20个分类器
        for i in range(1,31):#bins=10,(1,11);bins=15,(1,16);bins=20,(1,21);bins=25,(1,26);bins=30,(1,31);bins=35,(1,36)
            if i == 1:
               groups = [31,61]#bins=10,[11,21,31,41,51,61,71,81];bins=15,[16,31,46,61,76];bins=20,[21,41,61,81];bins=25,[26,51,76];bins=30,[31,61];bins=35,[36,71]
            else:
               groups = list(range(i, 91, 30))#bins=10,(i, 91, 10);bins=15,(i, 91, 15);bins=20,(i, 91, 20);bins=25,(i, 91, 25);bins=30,(i, 91, 30)
            y_train_groups = age_groups(y_train, groups)
            clf = RandomForestClassifier(n_estimators=100)#可选择不同分类器
        #RandomForestClassifier(n_estimators=100)
        #LogisticRegression()
        #LinearDiscriminantAnalysis()
        #KNeighborsClassifier(n_neighbors=5)
        #DecisionTreeClassifier()
        #AdaBoostClassifier(algorithm='SAMME',n_estimators=100)
            clf.fit(X_train, y_train_groups)
            classifiers.append((clf, groups))
        votes_test = np.zeros((X_test.shape[0], 90), dtype=int)#测试集票数存储
        for clf, groups in classifiers:
            y_pred_test_groups = clf.predict(X_test)  # 进行组别预测
            for idx, group in enumerate(y_pred_test_groups):
                start = groups[group - 1] if group > 0 else 1
                end = groups[group] if group < len(groups) else 90
                votes_test[idx, start:end] += 1  # 进行投票，确定组别之后，确定起始，所属年龄段各+1票
        y_pred = np.argmax(votes_test, axis=1)#选出最高票数对应的年龄
        mae = mean_absolute_error(y_test, y_pred)#计算当前折的MAE
        r2 = r2_score(y_test, y_pred)#计算当前折的R2
        fold_mae.append(mae)#存储到相应的存储表格
        fold_r2.append(r2)#存储到相应的存储表格
        for idx, pred_age in zip(test_index, y_pred):
            predicted_ages[idx, iteration] = pred_age
#输出预测结果
average_predicted_ages = np.mean(predicted_ages, axis=1)#计算平均预测年龄
#output_data = data[['ID'] + list(X.columns) +['gender']+['ethnicity'] + ['age']].copy()
output_data = data[['ID'] + list(X.columns) +['Dummy_1']+['Dummy_2'] + ['age']].copy()
output_data['Predicted_Age'] = average_predicted_ages#创建包含ID，10个CpG值，实际年龄，预测年龄的DataFrame
output_file_path_predictions = r"C:\Users\32766\Desktop\三平台无哑变量_prediction_results.xlsx"
output_data.to_excel(output_file_path_predictions, index=False)
print(f"预测年龄结果已输出到Excel文件: {output_file_path_predictions}")
print(predicted_ages)