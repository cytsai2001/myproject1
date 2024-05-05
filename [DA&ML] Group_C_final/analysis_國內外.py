import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Read dataset and clean the data
# all_2 for basically all analysis
# all_3 for adult and runtime
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
# # Plot the revenue and cumulative sales comparison
# plt.figure(figsize=(10, 6))
# plt.scatter(merged_comparison['Revenue'], merged_comparison['累計銷售金額'])
# plt.xlabel('Revenue')
# plt.ylabel('Cumulative Sales')
# plt.title('Comparison of Revenue and Cumulative Sales')
# plt.show()

ax = sns.regplot(x=np.log10(merged_comparison['Revenue']), y=np.log10(merged_comparison['累計銷售金額']))
ax.set_xlabel('Global Revenue (log scale)')
ax.set_ylabel('Domestic Revenue (log scale)')
ax.set_title('Correlation: Domestic Revenue vs Global Revenue')
plt.show()
plt.savefig("domestic_result_reg.png")

# 分開執行，才能存圖
plt.figure(figsize=(10, 6))
plt.boxplot([merged_comparison['Revenue'], merged_comparison['累計銷售金額']], labels=['Global Revenue', 'Domestic Revenue'])
plt.yscale('log')
plt.ylabel('Revenue (log scale)')
plt.title('Distribution of Global Revenue and Domestic Revenue')
# Label mean values
boxplot_data = [merged_comparison['Revenue'], merged_comparison['累計銷售金額']]
means = [np.mean(data) for data in boxplot_data]
for i, mean in enumerate(means):
    plt.text(i + 1, mean, f'Mean: {mean:.2f}', ha='center', va='bottom', color='black')
plt.show()
plt.savefig("domestic_result_box.png")
