import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Load BM.xlsx into a pandas DataFrame
df = pd.read_excel('BM.xlsx')

# Replace NaN values with the last non-NaN value
df['BM'].fillna(method='ffill', inplace=True)

# Find the best number of components using the Bayesian Information Criterion (BIC)
n_components = np.arange(1, 20)
models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(df['BM'].values.reshape(-1, 1)) for n in n_components]
bics = [model.bic(df['BM'].values.reshape(-1, 1)) for model in models]
best_n = n_components[np.argmin(bics)]

# Fit the BM time trace using the best number of components
gmm = GaussianMixture(best_n, covariance_type='full', random_state=0)
gmm.fit(df['BM'].values.reshape(-1, 1))

# Predict the states of the BM time trace
states = gmm.predict(df['BM'].values.reshape(-1, 1))

# Calculate the dwell times of the BM states
dwell_times = []
start_time = df['Time'][0]
for i in range(1, len(df)):
    if states[i] != states[i-1]:
        dwell_times.append(df['Time'][i] - start_time)
        start_time = df['Time'][i]

# Plot the fitting result and the distribution of dwell times
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(df['Time'], df['BM'], c=states, marker='_', cmap='viridis')
plt.xlabel('Time')
plt.ylabel('BM')
plt.title('Fitting Result')

plt.subplot(122)
plt.hist(dwell_times, bins=20)
plt.xlabel('Dwell Time')
plt.ylabel('Count')
plt.title('Distribution of Dwell Times')
plt.show()
