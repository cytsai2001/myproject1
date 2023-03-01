import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from excel file into pandas DataFrame
df = pd.read_excel("signal.xlsx")
signal = df['Signal'].values
time = df['Time'].values

# Define a step-finding algorithm
def step_finding_algorithm(signal):
    # Set a threshold to determine if a change in the signal is significant
    threshold = np.std(signal)

    # Initialize arrays to store the step start and end indices
    step_starts = []
    step_ends = []

    # Initialize variables to keep track of the current step start and end indices
    step_start = 0
    step_end = 0

    # Iterate over the signal values
    for i in range(1, len(signal)):
        # Check if the current change in the signal is greater than the threshold
        if abs(signal[i] - signal[i-1]) > threshold:
            # If the current change is greater than the threshold,
            # update the step end index and store the step start and end indices
            step_end = i
            step_starts.append(step_start)
            step_ends.append(step_end)
            step_start = i

    # Add the final step start and end indices
    step_starts.append(step_start)
    step_ends.append(len(signal) - 1)

    return step_starts, step_ends

# Apply the step-finding algorithm to the BM signal
step_starts, step_ends = step_finding_algorithm(signal)

# Calculate the dwell times by subtracting the time at each step end with the time at the corresponding step start
dwell_times = time[step_ends] - time[step_starts]

# Plot the BM signal and the steps
plt.plot(time, signal, 'b-', label='BM signal')
for i in range(len(step_starts)):
    plt.axvline(x=time[step_starts[i]], color='r', linestyle='--', label='Step starts' if i == 0 else '')
    plt.axvline(x=time[step_ends[i]], color='g', linestyle='--', label='Step ends' if i == 0 else '')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('BM signal and steps')
plt.legend()
plt.show()

# Plot the distribution of dwell times
plt.hist(dwell_times, bins=50)
plt.xlabel('Dwell time')
plt.ylabel('Count')
plt.title('Distribution of dwell times')
plt.show()
