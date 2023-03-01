import pandas as pd
import matplotlib.pyplot as plt

# Load the signal data from an Excel file into a pandas DataFrame
df = pd.read_excel("signal.xlsx")

# Define the column that contains the time values
time_column = "Time"

# Define the column that contains the signal values
signal_column = "Signal"

# Determine the states by thresholding the signal values
threshold = 0.5
df["State"] = (df[signal_column] > threshold).astype(int)

# Calculate the dwell time for each state (0 or 1) by taking the difference between the
# time when the state changes and the previous time
dwell_times = []
current_state = df["State"][0]
start_time = df[time_column][0]

for i in range(1, len(df)):
    if df["State"][i] != current_state:
        end_time = df[time_column][i]
        dwell_time = end_time - start_time
        dwell_times.append((current_state, dwell_time))
        current_state = df["State"][i]
        start_time = end_time

# Plot the signal and state time traces
fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].plot(df[time_column], df[signal_column])
ax[0].set_ylabel("Signal")

ax[1].step(df[time_column], df["State"], where="post")
ax[1].set_ylabel("State")
ax[1].set_xlabel("Time")

plt.show()
