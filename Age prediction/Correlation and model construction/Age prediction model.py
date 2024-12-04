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
os.chdir(r"C:\Users\32766\Desktop")
data = pd.read_excel(r"283.xlsx", header=0)
X = data.drop(['age', 'ID'], axis=1)
y = data['age']
IDs = data['ID']
repeats = 5
cv_folds = 10
predicted_ages = np.zeros((len(y), repeats))
for iteration in range(repeats):
    kf = KFold(n_splits=cv_folds, shuffle=True)
    fold_mae = []
    fold_r2 = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        ID_test = IDs.iloc[test_index]
        # Age group definition function
        def age_groups(y, groups):
            bins = np.concatenate(([1], groups, [91]))
            return np.digitize(y, bins)-1
        #All classifiers
        classifiers = []
        for i in range(1,31):#bins=10,(1,11);bins=15,(1,16);bins=20,(1,21);bins=25,(1,26);bins=30,(1,31);bins=35,(1,36)
            if i == 1:
               groups = [31,61]#bins=10,[11,21,31,41,51,61,71,81];bins=15,[16,31,46,61,76];bins=20,[21,41,61,81];bins=25,[26,51,76];bins=30,[31,61];bins=35,[36,71]
            else:
               groups = list(range(i, 91, 30))#bins=10,(i, 91, 10);bins=15,(i, 91, 15);bins=20,(i, 91, 20);bins=25,(i, 91, 25);bins=30,(i, 91, 30)
            y_train_groups = age_groups(y_train, groups)
            clf = RandomForestClassifier(n_estimators=100)
            clf.fit(X_train, y_train_groups)
            classifiers.append((clf, groups))
        votes_test = np.zeros((X_test.shape[0], 90), dtype=int)
        for clf, groups in classifiers:
            y_pred_test_groups = clf.predict(X_test)  # Perform group prediction
            for idx, group in enumerate(y_pred_test_groups):
                start = groups[group - 1] if group > 0 else 1
                end = groups[group] if group < len(groups) else 90
                votes_test[idx, start:end] += 1  # Perform voting to determine the group, then, once the group is determined, assign +1 vote to the corresponding starting point and the relevant age range
        y_pred = np.argmax(votes_test, axis=1) # Select the age corresponding to the highest vote count
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        fold_mae.append(mae)
        fold_r2.append(r2)
        for idx, pred_age in zip(test_index, y_pred):
            predicted_ages[idx, iteration] = pred_age
average_predicted_ages = np.mean(predicted_ages, axis=1) # Calculate the average predicted age
output_data = data[['ID'] + list(X.columns) + ['age']].copy()
output_data['Predicted_Age'] = average_predicted_ages
output_file_path_predictions = r"C:\Users\32766\Desktop\prediction_results.xlsx"
output_data.to_excel(output_file_path_predictions, index=False)