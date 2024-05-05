from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('all_3.csv')
df = df[(df['Budget'] > 100000) & (df['Revenue'] > 100000)]

# Step 2.1: Calculate benefit and create Benefit column
df['Benefit'] = df.apply(lambda row: row['Revenue'] - row['Budget'], axis=1)

X = df[['Budget', 'runtime']]
Y = df['Revenue']

ratios = range(5, 100, 5)

model = LinearRegression()

fig, axes = plt.subplots(1, figsize=(8, 6))

mse_scores = []
mape_scores = []

for ratio in ratios:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=(100-ratio)/100, random_state=2023)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mse_scores.append(mse)
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mape_scores.append(mape)

# Plot mean squared error
axes.plot(ratios, mape_scores, label='Mean Absolute Percentage Error')
axes.set_title(model.__class__.__name__)
axes.set_xlabel('Training Data Ratio (%)')
axes.set_ylabel('Mean Absolute Percentage Error (%)')
axes.legend()

print(f'{model.__class__.__name__}:')
print(f'Minimum Mean Squared Error: {min(mse_scores)} at {ratios[mse_scores.index(min(mse_scores))]}')
print(f'Minimum Mean Squared Error: {min(mape_scores)} at {ratios[mape_scores.index(min(mape_scores))]}')
plt.tight_layout()
plt.show()
plt.savefig("ML_performance_var_ratio.png")

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=(100-ratios[mape_scores.index(min(mape_scores))])/100, random_state=2023)

model = LinearRegression()
model.fit(X_train, y_train)

budget = float(input('Enter the budget: '))
runtime = float(input('Enter the runtime: '))

# Predict revenue for user-provided values
input_data = [[budget, runtime]]
predicted_revenue = model.predict(input_data)

print(f'Predicted Revenue: {predicted_revenue[0]}')
