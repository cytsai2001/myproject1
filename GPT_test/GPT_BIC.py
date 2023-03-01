import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("BM.xlsx")

# Replace NaN values with the last non-NaN value
df.fillna(method='ffill', inplace=True)

# Get time and BM signals
time = df['Time'].values
BM = df['BM'].values

# Determine the best number of components using BIC
bic = []
for n_components in range(1, 11):
    gmm = GaussianMixture(n_components=n_components)
    gmm.fit(BM.reshape(-1, 1))
    bic.append(gmm.bic(BM.reshape(-1, 1)))

best_n_components = np.argmin(bic) + 1
print("The best number of components is:", best_n_components)

# Fit BM signal using the best number of components
gmm = GaussianMixture(n_components=6)
gmm.fit(BM.reshape(-1, 1))

# Get the means, standard deviations, and weights of the components
means = gmm.means_.flatten()
stds = np.sqrt(gmm.covariances_.flatten())
weights = gmm.weights_

# Sort the components by their means
sort_idx = np.argsort(means)
means = means[sort_idx]
stds = stds[sort_idx]
weights = weights[sort_idx]

# Plot the fitted results
plt.plot(time, BM, label="BM time trace")
for i, (mean, std) in enumerate(zip(means, stds)):
    plt.plot(time, gmm.predict_proba(BM.reshape(-1, 1))[:, i] * mean, '.', label=f"Component {i+1}")

plt.legend()
plt.show()
