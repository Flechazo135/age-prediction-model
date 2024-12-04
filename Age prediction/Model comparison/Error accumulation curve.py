import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib.lines import Line2D
plt.style.use('ggplot')
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = False
plt.rcParams['axes.grid.axis'] = 'both'
plt.rcParams['axes.grid.which'] = 'major'
plt.rcParams['font.family'] = 'Times New Roman'
os.chdir(r"C:\Users\32766\Desktop")
file_path = 'models.xlsx'
data= pd.read_excel(file_path)
errors_model_1 = data[data['Models'] == 'AdaBoost']['Absolute error'].values
errors_model_2 = data[data['Models'] == 'Ensemble']['Absolute error'].values
errors_model_3 = data[data['Models'] == 'MLR']['Absolute error'].values
errors_model_4 = data[data['Models'] == 'RFR']['Absolute error'].values
errors_model_5 = data[data['Models'] == 'Ridge']['Absolute error'].values
errors_model_6 = data[data['Models'] == 'SVR']['Absolute error'].values
errors_model_7 = data[data['Models'] == 'XGBoost']['Absolute error'].values
# Calculate the cumulative error distribution for each model
def cumulative_error_distribution(errors):
    errors_sorted = np.sort(errors)
    cumulative_percentage = np.arange(1, len(errors) + 1) / len(errors)
    return errors_sorted, cumulative_percentage
errors_sorted_1, cum_percentage_1 = cumulative_error_distribution(errors_model_1)
errors_sorted_2, cum_percentage_2 = cumulative_error_distribution(errors_model_2)
errors_sorted_3, cum_percentage_3 = cumulative_error_distribution(errors_model_3)
errors_sorted_4, cum_percentage_4 = cumulative_error_distribution(errors_model_4)
errors_sorted_5, cum_percentage_5 = cumulative_error_distribution(errors_model_5)
errors_sorted_6, cum_percentage_6 = cumulative_error_distribution(errors_model_6)
errors_sorted_7, cum_percentage_7 = cumulative_error_distribution(errors_model_7)
# Plot the cumulative error curves for multiple data sets
plt.figure(figsize=(9, 6))
plt.plot(errors_sorted_1, cum_percentage_1, label='AdaBoost',color='#3C78BA',markersize=2.5,linewidth=1)
plt.plot(errors_sorted_2, cum_percentage_2, label='Ensemble',color='#7150B4', markersize=2.5,linewidth=1)
plt.plot(errors_sorted_3, cum_percentage_3, label='MLR', color='#E69F00', markersize=2.5,linewidth=1)
plt.plot(errors_sorted_4, cum_percentage_4, label='RFR',color='#359787', markersize=2.5,linewidth=1)
plt.plot(errors_sorted_5, cum_percentage_5, label='Ridge', color='#C63D18',  markersize=2.5,linewidth=1)
plt.plot(errors_sorted_6, cum_percentage_6, label='SVR', color='#EC7D0E', markersize=2.5,linewidth=1)
plt.plot(errors_sorted_7, cum_percentage_7, label='XGBoost', color='#C63D18', markersize=2.5,linewidth=1)
# Find the error values corresponding to 90% cumulative proportion for each model
def find_error_at_90(cum_percentage, errors_sorted):
    index_90 = np.argmax(cum_percentage >= 0.9)
    return errors_sorted[index_90]
error_90_model_1 = find_error_at_90(cum_percentage_1, errors_sorted_1)
error_90_model_2 = find_error_at_90(cum_percentage_2, errors_sorted_2)
error_90_model_3 = find_error_at_90(cum_percentage_3, errors_sorted_3)
error_90_model_4 = find_error_at_90(cum_percentage_4, errors_sorted_4)
error_90_model_5 = find_error_at_90(cum_percentage_5, errors_sorted_5)
error_90_model_6 = find_error_at_90(cum_percentage_6, errors_sorted_6)
error_90_model_7 = find_error_at_90(cum_percentage_7, errors_sorted_7)
plt.xlabel('Absolute Error (years)', fontsize=12, color='black')
plt.ylabel('Cumulative Proportion',fontsize=12, color='black')
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.legend()
plt.show()
print(error_90_model_1, error_90_model_2, error_90_model_3, error_90_model_4, error_90_model_5, error_90_model_6, error_90_model_7)
# Obtain the cumulative proportion for each model at a specified error value
def cumulative_percentage_at_error(errors_sorted, cum_percentage, error_value):
    index = np.searchsorted(errors_sorted, error_value, side='right') - 1
    if index >= 0 and index < len(cum_percentage):
        return cum_percentage[index]
    else:
        return None
error_values = [1,1.5,2,2.5,3,3.5,4,4.5,5]
for model_name, errors_sorted, cum_percentage in zip(
    ['AdaBoost', 'Ensemble', 'MLR', 'RFR', 'Ridge', 'SVR', 'XGBoost'],
    [errors_sorted_1, errors_sorted_2, errors_sorted_3, errors_sorted_4, errors_sorted_5, errors_sorted_6, errors_sorted_7],
    [cum_percentage_1, cum_percentage_2, cum_percentage_3, cum_percentage_4, cum_percentage_5, cum_percentage_6, cum_percentage_7]
):
    print(f"\n{model_name} Model:")
    for error_value in error_values:
        proportion = cumulative_percentage_at_error(errors_sorted, cum_percentage, error_value)
        print(f"Cumulative Proportion at {error_value} years error = {proportion:.4f}")
import matplotlib.pyplot as plt
errors = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
ada_boost = [0.1661, 0.2615, 0.3251, 0.3604, 0.4205, 0.4629, 0.5230, 0.5689, 0.6254]
ensemble = [0.1979, 0.2473, 0.3110, 0.3463, 0.4523, 0.5053, 0.5512, 0.5866, 0.6643]
mlr = [0.1519, 0.1979, 0.2686, 0.3110, 0.3816, 0.4205, 0.4700, 0.4912, 0.5583]
rfr = [0.1519, 0.2226, 0.2792, 0.3746, 0.4417, 0.5018, 0.5300, 0.5901, 0.6184]
ridge = [0.1131, 0.1484, 0.1943, 0.2827, 0.3498, 0.3993, 0.4417, 0.4700, 0.5088]
svr = [0.1095, 0.1625, 0.2367, 0.3004, 0.3463, 0.3816, 0.4629, 0.5018, 0.5477]
xgboost = [0.1307, 0.2261, 0.2862, 0.3604, 0.4417, 0.5088, 0.5406, 0.5830, 0.6325]
plt.figure(figsize=(5,6))
plt.plot(errors, ada_boost,label='AdaBoost',color='#3C78BA',marker='o',markersize=2.5,linewidth=1)
plt.plot(errors, ensemble,label='Ensemble',color='#7150B4',marker='o', markersize=2.5,linewidth=1)
plt.plot(errors, mlr, label='MLR', color='#E69F00',marker='o', markersize=2.5,linewidth=1)
plt.plot(errors, rfr, label='RFR',color='#359787',marker='o',markersize=2.5,linewidth=1)
plt.plot(errors, ridge, label='Ridge', color='#C63D18', marker='o',markersize=2.5,linewidth=1)
plt.plot(errors, svr, label='SVR', color='#EC7D0E',marker='o',markersize=2.5, linewidth=1)
plt.plot(errors, xgboost,label='XGBoost', color='#C63D18', marker='o',markersize=2.5,linewidth=1)
legend_lines = [
    Line2D([0], [0], color='#3C78BA', linewidth=2, label='AdaBoost'),
    Line2D([0], [0], color='#7150B4', linewidth=2, label='Ensemble'),
    Line2D([0], [0], color='#E69F00', linewidth=2, label='MLR'),
    Line2D([0], [0], color='#359787', linewidth=2, label='RFR'),
    Line2D([0], [0], color='#C63D18', linewidth=2, label='Ridge'),
    Line2D([0], [0], color='#EC7D0E', linewidth=2, label='SVR'),
    Line2D([0], [0], color='#C63D0E', linewidth=2, label='XGBoost')
]
plt.legend(handles=legend_lines)
plt.legend(handles=legend_lines)
plt.xlabel('Absolute Error (years)', fontsize=12, color='black')
plt.ylabel('Cumulative Proportion',fontsize=12, color='black')
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_edgecolor('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_edgecolor('black')
ax.spines['left'].set_linewidth(1.5)
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
plt.show()