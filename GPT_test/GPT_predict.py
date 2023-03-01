import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

# Load the BM time trace into a DataFrame
df = pd.read_excel('BM.xlsx')

# Replace NaN values with the last non-NaN value
df.fillna(method='ffill', inplace=True)

# Find the best number of components using the Bayesian Information Criterion (BIC)
n_components = np.arange(1, 20)
models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(df['BM'].values.reshape(-1, 1)) for n in n_components]
bics = [model.bic(df['BM'].values.reshape(-1, 1)) for model in models]
best_n = n_components[np.argmin(bics)]

# Define a function to fit the BM time trace using Gaussian Mixture Model
def fit_BM(df, n_components):
    gmm = GaussianMixture(n_components=n_components, covariance_type='full')
    gmm.fit(df[['BM']].values)
    return gmm

# Define a function to predict the steps in the BM time trace
def predict_steps(df, gmm):
    y_pred = gmm.predict(df[['BM']].values)
    y_pred = pd.DataFrame({'Time': df['Time'], 'BM': df['BM'], 'Step': y_pred})
    return y_pred

# Fit the BM time trace using Gaussian Mixture Model with n_components=2
gmm = fit_BM(df, n_components=best_n)

# Predict the steps in the BM time trace
y_pred = predict_steps(df, gmm)

# Plot the predicted steps
plt.figure()
for i in range(gmm.n_components):
    plt.plot(y_pred[y_pred['Step']==i]['Time'], y_pred[y_pred['Step']==i]['BM'], '.', label='Step {}'.format(i+1))
plt.legend()
plt.xlabel('Time')
plt.ylabel('BM')
plt.title('Predicted Steps in BM Time Trace')
plt.show()
