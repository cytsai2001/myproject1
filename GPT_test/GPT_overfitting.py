import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

# Load the data from the link
df = pd.read_excel('BM.xlsx')

# Replace NaN values with the last non-NaN value
df.fillna(method='ffill', inplace=True)

# Define the number of components to search over
n_components = np.arange(1, 15)

# Define the covariance type to search over
covariance_types = ['full', 'tied', 'diag', 'spherical']

# Define the hyperparameters to search over
param_grid = {'n_components': n_components, 'covariance_type': covariance_types}

# Create a Gaussian Mixture Model
gmm = GaussianMixture(random_state=0)

# Use GridSearchCV to find the best hyperparameters
gmm_cv = GridSearchCV(gmm, param_grid, cv=5)

# Fit the model to the data
gmm_cv.fit(df[['BM']].values)

# Predict the cluster assignments
df['cluster'] = gmm_cv.predict(df[['BM']].values)

# Plot the data
plt.scatter(df.index, df['BM'], c=df['cluster'])
plt.xlabel('Time')
plt.ylabel('BM')
plt.show()
