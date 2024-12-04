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
os.chdir(r"C:\Users\32766\Desktop")
data = pd.read_excel(r"450k+283all-1.xlsx", header=0)
X = data.drop(['age', 'ID','gender','ethnicity'], axis=1)
y = data['age']
IDs = data['ID']
repeats = 5
cv_folds = 10
all_fold_mae_results = []
all_fold_r2_results = []
mean_mae_results = []
mean_r2_results = []
predicted_ages = np.zeros((len(y), repeats))
for iteration in range(repeats):
    kf = KFold(n_splits=cv_folds, shuffle=True)
    fold_mae = []
    fold_r2 = []
    # Cross-validation
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
        model = model.fit(X_train, y_train)  # fit
        y_pred = model.predict(X_test)  # predicti
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        fold_mae.append(mae)
        fold_r2.append(r2)
        for idx, pred_age in zip(test_index, y_pred):
            predicted_ages[idx, iteration] = pred_age
    all_fold_mae_results.append(fold_mae)
    all_fold_r2_results.append(fold_r2)
    mean_mae = np.mean(fold_mae)
    mean_r2 = np.mean(fold_r2)
    mean_mae_results.append(mean_mae)
    mean_r2_results.append(mean_r2)
overall_mean_mae = np.mean(mean_mae_results)
overall_mean_r2 = np.mean(mean_r2_results)
average_predicted_ages = np.mean(predicted_ages, axis=1)
output_data = data[['ID'] + list(X.columns) + ['age']].copy()
output_data['Predicted_Age'] = average_predicted_ages
output_file_path_predictions = r"RFR-831_prediction_results.xlsx"
output_data.to_excel(output_file_path_predictions, index=False)