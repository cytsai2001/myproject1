import os
import pandas as pd

# Define the directory where the CSV files are located
directory = './for_csv_3'

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Loop through each CSV file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the CSV file into a DataFrame
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)

        # Append the DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)

# Write the combined DataFrame to a new CSV file
combined_df.to_csv('all_3.csv', index=False)
