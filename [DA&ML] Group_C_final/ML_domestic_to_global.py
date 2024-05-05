from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have loaded and preprocessed the data in merged_comparison DataFrame

df = pd.read_csv('all_3.csv')
df = df[(df['Budget'] > 100000) & (df['Revenue'] > 100000)]

# Step 2.1: Calculate benefit and create Benefit column
df['Benefit'] = df.apply(lambda row: row['Revenue'] - row['Budget'], axis=1)

df1 = pd.read_csv('20180730_20230507.csv')
df2 = pd.read_csv('107107.csv')

df1.drop('上映院數', axis=1, inplace=True)
df1.drop('銷售票數', axis=1, inplace=True)
df1.drop('周票數變動率', axis=1, inplace=True)
df1.drop('銷售金額', axis=1, inplace=True)
df1 = df1.drop_duplicates(subset=['中文片名'], keep='first')

mask = df2['中文片名'].str.contains('\n', na=False)

split_values = df2.loc[mask, '中文片名'].str.split('\n', expand=True)[1]

df2.loc[mask, '外文片名'] = split_values

df2 = df2.drop_duplicates(subset=['中文片名'], keep='first')

mask = df2['中文片名'].str.contains('\n', na=False)

df2.loc[mask, '中文片名'] = df2.loc[mask, '中文片名'].str.split('\n', n=1).str[0]

mask = True

df1['中文片名'] = df1['中文片名'].str.strip()
df2['中文片名'] = df2['中文片名'].str.strip()

merged_data = pd.merge(df1, df2, on='中文片名', how='left')

common_titles = df['Title'].isin(merged_data['外文片名'])
common_titles_list = df.loc[common_titles, 'Title'].tolist()
common_movies_df = df.loc[common_titles, ['Title', 'Revenue']]
common_movies_merged = merged_data.loc[merged_data['外文片名'].isin(common_titles_list), ['外文片名', '累計銷售金額']]

# Merge the dataframes on the common movie titles
merged_comparison = pd.merge(common_movies_df, common_movies_merged, left_on='Title', right_on='外文片名', how='inner')
merged_comparison['累計銷售金額'] = merged_comparison['累計銷售金額']//30

X = merged_comparison[['累計銷售金額']]  # Input feature
Y = merged_comparison['Revenue']  # Target variable

ratios = range(5, 100, 5)
mape_scores = []

for ratio in ratios:
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=(100 - ratio) / 100, random_state=2023)

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on test data
    y_pred = model.predict(X_test)

    # Calculate MAPE
    mape = mean_absolute_percentage_error(y_test, y_pred)
    mape_scores.append(mape)

# Plot MAPE against training data ratio
plt.plot(ratios, mape_scores)
plt.title('MAPE vs Training Data Ratio')
plt.xlabel('Training Data Ratio (%)')
plt.ylabel('Mean Absolute Percentage Error (%)')
plt.show()
plt.savefig("ML_domestic_perform.png")

min_mape_ratio = ratios[np.argmin(mape_scores)]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=(100 - min_mape_ratio) / 100, random_state=2023)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test data
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print('Evaluation Metrics:')
print(f'Mean Squared Error: {mse:.2f}')
print(f'Mean Absolute Percentage Error: {mape:.2f}')

# Predict revenue for user-provided values
budget = float(input('Enter the 累計銷售金額: '))
input_data = [[budget]]
predicted_revenue = model.predict(input_data)

print(f'Predicted Revenue: {predicted_revenue[0]}')
