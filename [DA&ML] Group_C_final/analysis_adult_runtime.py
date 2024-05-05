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

# Step 3: Perform correlation analysis and plot the results
fig, axes = plt.subplots(2, 4, figsize=(240, 12))

# Perform correlation analysis and plot the results
sns.regplot(x=df['runtime'], y=np.log10(df['Popularity']), ax=axes[0, 0])
axes[0, 0].set_xlabel('Duration')
axes[0, 0].set_ylabel('Popularity (log scale)')
axes[0, 0].set_title('Correlation: Popularity vs Duration')

sns.regplot(x=df['runtime'], y=df['vote_average'], ax=axes[0, 1])
axes[0, 1].set_xlabel('Duration')
axes[0, 1].set_ylabel('Vote Average')
axes[0, 1].set_title('Correlation: Vote Average vs Duration')

sns.regplot(x=df['runtime'], y=np.log10(df['Revenue']), ax=axes[0, 2])
axes[0, 2].set_xlabel('Duration')
axes[0, 2].set_ylabel('Revenue (log scale)')
axes[0, 2].set_title('Correlation: Duration vs Revenue')

sns.regplot(x=df['runtime'], y=np.log10(df['Benefit']), ax=axes[0, 3])
axes[0, 3].set_xlabel('Duration')
axes[0, 3].set_ylabel('Benefit (log scale)')
axes[0, 3].set_title('Correlation: Duration vs Benefit')

sns.boxplot(x=df['adult'], y=np.log10(df['Popularity']), ax=axes[1, 0])
axes[1, 0].set_xlabel('Adult or not')
axes[1, 0].set_ylabel('Popularity (log scale)')
axes[1, 0].set_title('Boxplot: Adult or not vs Popularity')

sns.boxplot(x=df['adult'], y=df['vote_average'], ax=axes[1, 1])
axes[1, 1].set_xlabel('Adult or not')
axes[1, 1].set_ylabel('Vote average')
axes[1, 1].set_title('Boxplot: Adult or not vs Vote average')

sns.boxplot(x=df['adult'], y=np.log10(df['Revenue']), ax=axes[1, 2])
axes[1, 2].set_xlabel('Adult or not')
axes[1, 2].set_ylabel('Revenue (log scale)')
axes[1, 2].set_title('Correlation: Adult or not vs Revenue')

# Step 3.6: Box plots for different production_companies and their distribution of Revenue (log scale) as y-axis
sns.boxplot(x=df['adult'], y=np.log10(df['Benefit']), ax=axes[1, 3])
axes[1, 3].set_xlabel('Adult or not')
axes[1, 3].set_ylabel('Benefit (log scale)')
axes[1, 3].set_title('Boxplot: Adult or not vs Benefit')

plt.tight_layout()
plt.savefig("3_result.png")
plt.show()

sns.boxplot(y=df['runtime'])
runtime_quartiles = df['runtime'].describe().loc[['25%', '50%', '75%']]
print(runtime_quartiles)

