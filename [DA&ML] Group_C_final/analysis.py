import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Read dataset and clean the data
# all_2 for basically all analysis
# all_3 for adult and runtime
df = pd.read_csv('all_3.csv')
df = df[(df['Budget'] > 100000) & (df['Revenue'] > 100000)]
# df = df[(df['Budget'] != 0) & (df['Revenue'] != 0)]

# Step 2: Calculate length of TW_stream_providers and create Stream column
df['Stream'] = df['TW_stream_providers'].apply(lambda x: len(eval(x)) if isinstance(x, str) and x.strip("[]") else 0)

# Step 2.1: Calculate benefit and create Benefit column
df['Benefit'] = df.apply(lambda row: row['Revenue'] - row['Budget'], axis=1)

# Create a new list to store the data
data = []

# Iterate over each row in the original DataFrame
for _, row in df.iterrows():
    companies = eval(row['production_companies'])  # Convert string to list
    for company in companies:
        # Create a new dictionary for each production company
        new_row = row.copy()
        new_row['production_companies'] = company
        data.append(new_row)

# Create the new DataFrame
df_companies = pd.DataFrame(data)

# Reset index of df_companies
df_companies = df_companies.reset_index(drop=True)

# Step 3: Perform correlation analysis and plot the results
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# Perform correlation analysis and plot the results
sns.regplot(x=np.log10(df['Budget']), y=np.log10(df['Popularity']), ax=axes[0, 0])
axes[0, 0].set_xlabel('Budget (log scale)')
axes[0, 0].set_ylabel('Popularity (log scale)')
axes[0, 0].set_title('Correlation: Popularity vs Budget')

sns.regplot(x=np.log10(df['Revenue']), y=df['vote_average'], ax=axes[0, 1])
axes[0, 1].set_xlabel('Revenue (log scale)')
axes[0, 1].set_ylabel('Vote Average')
axes[0, 1].set_title('Correlation: Vote Average vs Revenue')

sns.boxplot(x=df['genre'], y=np.log10(df['Revenue']), ax=axes[1, 0])
axes[1, 0].set_xlabel('Genre')
axes[1, 0].set_ylabel('Revenue (log scale)')
axes[1, 0].set_title('Correlation: Genre vs Revenue')

sns.boxplot(x=df['genre'], y=np.log10(df['Popularity']), ax=axes[1, 1])
axes[1, 1].set_xlabel('Genre')
axes[1, 1].set_ylabel('Popularity (log scale)')
axes[1, 1].set_title('Correlation: Genre vs Popularity')

# sns.regplot(x=df['Stream'], y=np.log10(df['Popularity']), ax=axes[2, 0])
# axes[2, 0].set_xlabel('Stream')
# axes[2, 0].set_ylabel('Popularity (log scale)')
# axes[2, 0].set_title('Correlation: Popularity vs Stream')

sns.boxplot(x=df['Stream'], y=np.log10(df['Revenue']), ax=axes[2, 0])
axes[2, 0].set_xlabel('Stream')
axes[2, 0].set_ylabel('Revenue (log scale)')
axes[2, 0].set_title('Correlation: Revenue vs Stream')

# Step 4: Calculate average revenue for movies made by companies
average_revenue = df_companies.groupby('production_companies')['Revenue'].mean()
movie_counts = df_companies['production_companies'].value_counts()

# Step 5: Sort companies based on average revenue in descending order and select top 15 companies with more than one movie
top_15_companies = average_revenue[movie_counts > 1].sort_values(ascending=False).head(15)

# Include "20th Century Fox" in the top companies list
top_15_companies['20th Century Fox'] = average_revenue.loc["20th Century Fox"]

# Step 6: Filter df_companies to include only movies made by top 15 companies (including "20th Century Fox")
top_15_movies = df_companies[df_companies['production_companies'].isin(top_15_companies.index)]

# Step 7: Sort the top 15 companies based on average revenue in descending order
top_15_movies['production_companies'] = pd.Categorical(top_15_movies['production_companies'], categories=top_15_companies.index, ordered=True)
top_15_movies.sort_values(by='production_companies', inplace=True)

# Step 3.6: Box plots for different production_companies and their distribution of Revenue (log scale) as y-axis
sns.boxplot(x=top_15_movies['production_companies'], y=np.log10(top_15_movies['Revenue']), ax=axes[2, 1])
axes[2, 1].set_xlabel('Production Companies')
axes[2, 1].set_ylabel('Revenue (log scale)')
axes[2, 1].set_title('Boxplot: Production Companies vs Revenue')


# Rotate x-axis labels for better visibility
axes[1, 0].tick_params(axis='x', rotation=90)
axes[2, 1].tick_params(axis='x', rotation=90)


plt.tight_layout()
plt.savefig("3_result.png")
plt.show()


# # Step 4: Calculate average revenue for movies made by companies
# average_revenue = df_companies.groupby('production_companies')['Revenue'].mean()
# movie_counts = df_companies['production_companies'].value_counts()
#
# # Step 5: Sort companies based on average revenue in descending order and select top 15 companies with more than one movie
# top_15_companies = average_revenue[movie_counts > 1].sort_values(ascending=False).head(15)
#
# # Include "20th Century Fox" in the top companies list
# top_15_companies['20th Century Fox'] = average_revenue.loc["20th Century Fox"]
#
# # Step 6: Filter df_companies to include only movies made by top 15 companies (including "20th Century Fox")
# top_15_movies = df_companies[df_companies['production_companies'].isin(top_15_companies.index)]
#
# # Step 7: Sort the top 15 companies based on average revenue in descending order
# top_15_movies['production_companies'] = pd.Categorical(top_15_movies['production_companies'], categories=top_15_companies.index, ordered=True)
# top_15_movies.sort_values(by='production_companies', inplace=True)
#
# # Step 8: Plot box plot of revenue for top 15 companies (including "20th Century Fox")
# plt.figure(figsize=(12, 6))
# sns.boxplot(x=top_15_movies['production_companies'], y=np.log10(top_15_movies['Revenue']))
# plt.xlabel('Production Companies')
# plt.ylabel('Revenue (log scale)')
# plt.title('Boxplot: Revenue for Top 15 Companies (with more than one movie) including 20th Century Fox')
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()
# plt.savefig("top_15_revenue_companies.png")


# Create a new DataFrame df_year
df_year = df.copy()

# Extract the year from the 'Release Date' column and assign it to 'Release Year'
df_year['Release Date'] = pd.to_datetime(df_year['Release Date'])
df_year['Release Year'] = df_year['Release Date'].dt.year

# Filter the data for movies with Budget and Revenue > 100000
df_filtered = df_year[(df_year['Budget'] > 100000) & (df_year['Revenue'] > 100000)]

# Create subplots for box plots
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Box plot for Budget
sns.boxplot(x='Release Year', y='Budget', data=df_filtered, ax=axes[0])
axes[0].set_xlabel('Year')
axes[0].set_ylabel('Budget')
axes[0].set_title('Distribution of Budget (>100,000) by Year')
axes[0].set_yscale('log')

# Box plot for Revenue
sns.boxplot(x='Release Year', y='Revenue', data=df_filtered, ax=axes[1])
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Revenue')
axes[1].set_title('Distribution of Revenue (>100,000) by Year')
axes[1].set_yscale('log')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()
plt.savefig("3_18-23_budget_and_revenue.png")
