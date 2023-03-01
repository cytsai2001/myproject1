import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Load data into a DataFrame
df = pd.read_excel('BM.xlsx')

# Replace NaN values with last non-NaN signal
df.fillna(method='ffill', inplace=True)

# Get the signal values
signal = df['Signal'].values

# Fit the Gaussian Mixture Model
gm = GaussianMixture(n_components=5)
gm.fit(signal.reshape(-1, 1))

# Predict the states
states = gm.predict(signal.reshape(-1, 1))

# Calculate the dwell times
dwell_times = []
start_time = df['Time'][0]
for i in range(1, len(df)):
    if states[i] != states[i - 1]:
        dwell_times.append(df['Time'][i] - start_time)
        start_time = df['Time'][i]

# Plot the fitting result
plt.plot(df['Time'], signal, label='BM signal')
plt.plot(df['Time'], states*20, label='BM states')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.legend()
plt.show()

# Plot the distribution of dwell times
plt.hist(dwell_times, bins=20)
plt.xlabel('Dwell time')
plt.ylabel('Count')
plt.show()
