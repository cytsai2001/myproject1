import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
import scipy
import matplotlib


def main(path_to_parent_folder, BM_max=70, BM_min=130):
    # read step.txt and separate the lines by BMx_fixing_i
    beads = {}
    with open(path_to_parent_folder + '/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt', 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('BMx_fixing_'):
                fixing = line
                beads[fixing] = []
                i += 1
                while i < len(lines) and not lines[i].startswith('BMx_fixing_'):
                    beads[fixing].append(lines[i])
                    i += 1

    diffs = []
    discarded_bead_by_init = []
    bead = 0
    while bead < len(beads):
        i = 0
        print(f'processing BMx_fixing_{bead}')
        while i < len(beads[f'BMx_fixing_{bead}']):
            if len(beads[f'BMx_fixing_{bead}']) > 1:
                # Check BM of step 0
                if i == 0 and (not BM_min <= float(beads[f'BMx_fixing_{bead}'][i].split("BM = ")[1].split(" ± ")[0]) <= BM_max):
                    discarded_bead_by_init.append(f'BMx_fixing_{bead}')
                    break

                try:
                    curr_line = beads[f'BMx_fixing_{bead}'][i]
                    curr_bm = float(curr_line.split("BM = ")[1].split(" ± ")[0])
                    next_i = i+1

                    # Look for the next valid step
                    while next_i < len(beads[f'BMx_fixing_{bead}']):
                        next_line = beads[f'BMx_fixing_{bead}'][next_i]
                        next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])

                        if 5 <= next_bm <= 150:
                            break
                        else:
                            next_i += 1

                    # Calculate difference between valid steps
                    if next_i < len(beads[f'BMx_fixing_{bead}']):
                        next_line = beads[f'BMx_fixing_{bead}'][next_i]
                        next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])
                        diff = next_bm - curr_bm
                        if 5 <= diff <= 150:
                            diffs.append(np.absolute(diff))

                    i = next_i

                except IndexError:
                    i += 1
                    continue
            else:
                break
        bead += 1

    # Use BIC to determine the optimal number of components
    bic = []
    n_components_range = range(1, 11)
    for n_components in n_components_range:
        gmm = GaussianMixture(n_components=n_components).fit(np.array(diffs).reshape(-1, 1))
        bic.append(gmm.bic(np.array(diffs).reshape(-1, 1)))

    # Plot the BIC scores
    plt.plot(n_components_range, bic, 'o-')
    plt.xlabel('Number of components')
    plt.ylabel('BIC score')
    plt.savefig(path_to_parent_folder + f"/BMx_fixing_Pelt3000_mean_deadtime_2/BIC.png"
                , dpi=300)

    # Fit the GMM with the optimal number of components
    # n_components_optimal = n_components_range[np.argmin(bic)]
    n_components_optimal = 5
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
    plt.savefig(path_to_parent_folder + f"/BMx_fixing_Pelt3000_mean_deadtime_2/step_size_fitting_manual_select_5.png"
                , dpi=300)
