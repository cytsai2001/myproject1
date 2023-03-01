import pandas as pd

# Load the time trace data from an Excel file into a pandas DataFrame
df = pd.read_excel("time_traces.xlsx")

# Define the column that contains the time values
time_column = "Time"

# Define the column that contains the state values (0 or 1)
state_column = "State"

# Calculate the dwell time for each state (0 or 1) by taking the difference between the
# time when the state changes and the previous time
dwell_times = []
current_state = df[state_column][0]
start_time = df[time_column][0]

for i in range(1, len(df)):
    if df[state_column][i] != current_state:
        end_time = df[time_column][i]
        dwell_time = end_time - start_time
        dwell_times.append((current_state, dwell_time))
        current_state = df[state_column][i]
        start_time = end_time

# Print the calculated dwell times
print("Dwell times:", dwell_times)
