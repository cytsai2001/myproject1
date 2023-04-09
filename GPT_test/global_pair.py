import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
from sklearn.mixture import GaussianMixture
from scipy.stats import kde
from scipy import stats
# matplotlib.use('TkAgg')


## ALL TOGETHER
step_files = [
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220924/1-2-836bp-0.5xRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220928/0924_s2_lane3_3-2-1162-ps-0.5x-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/0923_1895_0.5x/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt"
]

BM_max = 110
BM_min = 50

# read step.txt and separate the lines by BMx_fixing_i for each file
beads_dict_list = []
for step_file_path in step_files:
    beads = {}
    with open(step_file_path, 'r') as f:
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
            else:
                i += 1
    beads_dict_list.append(beads)

offset = 0
for i in range(1, len(beads_dict_list)):
    offset += len(beads_dict_list[i-1])
    for fixing in list(beads_dict_list[i].keys()):
        new_fixing = f'BMx_fixing_{int(fixing.split("_")[-1]) + offset}'
        beads_dict_list[i][new_fixing] = beads_dict_list[i].pop(fixing)

# combine the dictionaries into a single pooled dictionary
pooled_dict = {}
for beads_dict in beads_dict_list:
    for fixing, data in beads_dict.items():
        if fixing in pooled_dict:
            pooled_dict[fixing].extend(data)
        else:
            pooled_dict[fixing] = data

steps = {}
# create dictionary to store step info for each bead
bead_steps = {}

# loop through lines in file
for BMx_fixing, step_data in pooled_dict.items():
    bead_steps[BMx_fixing] = []
    for step_data_in_list in step_data:
        step_info = step_data_in_list.strip().split(',')
        # extract step number and BM value
        step_num = int(step_info[0].split()[1].strip(':'))
        step_bm = float(step_info[1].split('=')[1].split()[0])
        # add step info to list for current bead
        bead_steps[BMx_fixing].append((step_num, step_bm))

diffs = []
discarded_bead_by_init = {}
bead_steps_copy = bead_steps.copy()
for bead_name, steps in bead_steps.items():
    if not BM_min <= steps[0][1] <= BM_max:
        discarded_bead_by_init[bead_name] = bead_steps_copy.pop(bead_name)
    else:
        step = 0
        steps.remove(steps[0])
        while step < len(steps):
            if not 5 <= steps[step][1] <= 150:
                steps.remove(steps[step])
                step -= 1
            step += 1

# calculate pairwise differences for each bead
pairwise_diffs = []
for bead_name, steps in bead_steps_copy.items():
    for i in range(len(steps)):
        for j in range(i+1, len(steps)):
            diff = abs(steps[i][1] - steps[j][1])
            if 5 <= diff <= 100:
                pairwise_diffs.append(diff)

# # plot histogram of pairwise differences
# plt.hist(pairwise_diffs, bins=50)
# plt.xlabel("Pairwise differences in BM values")
# plt.ylabel("Frequency")
# plt.show()
# plt.savefig(path_to_parent_folder + f"/BMx_fixing_Pelt3000_mean_deadtime_2/pairwise.png"
#             , dpi=300)

# plt.figure()
# sns.kdeplot(pairwise_diffs, shade=True)
# plt.xlabel("BM pairwise differences")
# plt.ylabel("Density")
# plt.show()
# plot histogram of pairwise differences
plt.hist(pairwise_diffs, bins=50, alpha=0.5, density=True)

# fit KDE plot
density = kde.gaussian_kde(pairwise_diffs)
xs = np.linspace(0, 150, 200)
plt.plot(xs, density(xs), label='KDE plot')

# fit GMM plot
means = np.array([14.738, 26.089, 37.15, 48.843, 67.838, 90.905])
# n_components_optimal = 5
# gmm = GaussianMixture(n_components=n_components_optimal)
# gmm.fit(np.array(pairwise_diffs).reshape(-1, 1))
gmm = GaussianMixture(n_components=len(means), means_init=np.array(means).reshape(-1, 1)).fit(np.array(pairwise_diffs).reshape(-1, 1))
gmm_xs = np.linspace(0, 150, 200)
gmm_ys = np.exp(gmm.score_samples(gmm_xs.reshape(-1, 1)))
plt.plot(gmm_xs, gmm_ys, label='GMM plot')

for i in range(len(means)):
    mu = gmm.means_[i][0]
    sigma = np.sqrt(gmm.covariances_[i][0][0])
    weight = gmm.weights_[i]
    plt.plot(gmm_xs, weight * stats.norm.pdf(gmm_xs, mu, sigma),
             label=f"Gaussian {i+1}: μ = {mu:.2f}, σ = {sigma:.2f}")


# set plot labels and legend
plt.xlabel("Pairwise differences in BM values")
plt.ylabel("Density")
plt.legend()

# show and save plot
plt.show()
plt.savefig("global_pairwise.png", dpi=300)
