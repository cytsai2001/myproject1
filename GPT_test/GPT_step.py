import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
import scipy

with open('/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/BMx_fixing_Pelt/step.txt', 'r') as f:
    lines = f.readlines()

diffs = []

i = 0
while i < len(lines):
    # Check BM of step 0
    if i == 0 and (not 70 <= float(lines[i+1].split("BM = ")[1].split(" ± ")[0]) <= 130):
        i += 2
        continue

    try:
        curr_line = lines[i]
        curr_bm = float(curr_line.split("BM = ")[1].split(" ± ")[0])
        next_i = i+1

        # Look for the next valid step
        while next_i < len(lines):
            next_line = lines[next_i]
            next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])

            if 5 <= next_bm <= 200:
                break
            else:
                next_i += 1

        # Calculate difference between valid steps
        if next_i < len(lines):
            next_line = lines[next_i]
            next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])
            diff = next_bm - curr_bm
            diffs.append(np.absolute(diff))

        i = next_i

    except IndexError:
        i += 1
        continue

# Use BIC to determine the optimal number of components
bic = []
n_components_range = range(1, 7)
for n_components in n_components_range:
    gmm = GaussianMixture(n_components=n_components).fit(np.array(diffs).reshape(-1, 1))
    bic.append(gmm.bic(np.array(diffs).reshape(-1, 1)))

# Plot the BIC scores
plt.plot(n_components_range, bic, 'o-')
plt.xlabel('Number of components')
plt.ylabel('BIC score')
plt.show()

# Fit the GMM with the optimal number of components
n_components_optimal = n_components_range[np.argmin(bic)]
gmm = GaussianMixture(n_components=n_components_optimal).fit(np.array(diffs).reshape(-1, 1))
print("Optimal number of components:", n_components_optimal)

# Plot the histogram and GMM fitting
fig, ax = plt.subplots()
ax.hist(diffs, bins=50, density=True, alpha=0.5)
x = np.linspace(0, 200, 500).reshape(-1, 1)
logprob = gmm.score_samples(x)
pdf = np.exp(logprob)
ax.plot(x, pdf, '-k', label='GMM fitting')

# Plot each gaussian component
for i in range(n_components_optimal):
    pdf = gmm.weights_[i] * scipy.stats.norm(gmm.means_[i], np.sqrt(gmm.covariances_[i])).pdf(x)
    ax.plot(x, pdf, label=f'Gaussian component {i}'+f'\n{round(gmm.means_[i][0], 3)} ± {round(np.sqrt(gmm.covariances_[i][0][0]), 3)}'.format(i+1))

ax.legend()
plt.show()
plt.savefig(f"/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/BMx_fixing_Pelt/step_size_fitting_1.png"
            , dpi=300)
