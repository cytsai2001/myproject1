import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
import scipy
import os
import matplotlib
# matplotlib.use('TkAgg')


means = np.array([14.738, 26.089, 37.15, 48.843, 67.838, 90.905])

# Replace this list with the paths to your step.txt files
# # 1895 bp, 0.5X RRM
# step_files = [
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/0923_1895_0.5x/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20221123/slide1/4-1-1895bp-PS-150mMKCl-1.32uＭRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt"
# ]
# # 1162 bp, 0.5X RRM
# step_files = [
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220928/0924_s2_lane3_3-2-1162-ps-0.5x-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt"
# ]
# 836 bp, 0.5X RRM
step_files = [
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220924/1-2-836bp-0.5xRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
    "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt"
]

## ALL TOGETHER
# step_files = [
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220924/1-2-836bp-0.5xRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220928/0924_s2_lane3_3-2-1162-ps-0.5x-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/0923_1895_0.5x/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt",
#     "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20220916_s2_1-4-836bp-220nm-0.5xRRM/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt"
# ]

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

# offset = len(beads_dict_list[0])
# for fixing in list(beads_dict_list[1].keys()):
#     print(fixing)
#     new_fixing = f'new_BMx_fixing_{int(fixing.split("_")[-1]) + offset}'
#     print(new_fixing)
#     beads_dict_list[1][new_fixing] = beads_dict_list[1].pop(fixing)
#     print(beads_dict_list[1])
#
# for ne_fixing in list(beads_dict_list[1].keys()):
#     new_new_fixing = f'BMx_fixing_{int(ne_fixing.split("_")[-1])}'
#     beads_dict_list[1][new_new_fixing] = beads_dict_list[1].pop(ne_fixing)

# combine the dictionaries into a single pooled dictionary
pooled_dict = {}
for beads_dict in beads_dict_list:
    for fixing, data in beads_dict.items():
        if fixing in pooled_dict:
            pooled_dict[fixing].extend(data)
        else:
            pooled_dict[fixing] = data


diffs = []
discarded_bead_by_init = []
bead = 0
while bead < len(pooled_dict):
    i = 0
    print(f'processing BMx_fixing_{bead}')
    while i < len(pooled_dict[f'BMx_fixing_{bead}']):
        if len(pooled_dict[f'BMx_fixing_{bead}']) > 1:
            # Check BM of step 0
            if i == 0 and (not BM_min <= float(pooled_dict[f'BMx_fixing_{bead}'][i].split("BM = ")[1].split(" ± ")[0]) <= BM_max):
                discarded_bead_by_init.append(f'BMx_fixing_{bead}')
                break

            try:
                curr_line = pooled_dict[f'BMx_fixing_{bead}'][i]
                curr_bm = float(curr_line.split("BM = ")[1].split(" ± ")[0])
                next_i = i+1

                # Look for the next valid step
                while next_i < len(pooled_dict[f'BMx_fixing_{bead}']):
                    next_line = pooled_dict[f'BMx_fixing_{bead}'][next_i]
                    next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])

                    if 5 <= next_bm <= 110:
                        break
                    else:
                        next_i += 1

                # Calculate difference between valid steps
                if next_i < len(pooled_dict[f'BMx_fixing_{bead}']):
                    next_line = pooled_dict[f'BMx_fixing_{bead}'][next_i]
                    next_bm = float(next_line.split("BM = ")[1].split(" ± ")[0])
                    diff = next_bm - curr_bm
                    if 5 <= diff <= 110:
                        diffs.append(np.absolute(diff))

                i = next_i

            except IndexError:
                i += 1
                continue
        else:
            break
    bead += 1

# Use BIC to determine the optimal number of components
# bic = []
# n_components_range = range(1, 11)
# for n_components in n_components_range:
#     gmm = GaussianMixture(n_components=n_components).fit(np.array(diffs).reshape(-1, 1))
#     bic.append(gmm.bic(np.array(diffs).reshape(-1, 1)))

# # Plot the BIC scores
# plt.plot(n_components_range, bic, 'o-')
# plt.xlabel('Number of components')
# plt.ylabel('BIC score')
# plt.show()
# plt.savefig('Global_1895_0.5XRRM_BIC.png'
#             , dpi=300)

# Fit the GMM with the optimal number of components
# n_components_optimal = n_components_range[np.argmin(bic)]
# n_components_optimal = 6
gmm = GaussianMixture(n_components=len(means), means_init=np.array(means).reshape(-1, 1)).fit(np.array(diffs).reshape(-1, 1))

# print("Optimal number of components:", n_components_optimal)

# Plot the histogram and GMM fitting
fig, ax = plt.subplots()
ax.hist(diffs, bins=50, density=True, alpha=0.5)
x = np.linspace(0, 200, 500).reshape(-1, 1)
logprob = gmm.score_samples(x)
pdf = np.exp(logprob)
ax.plot(x, pdf, '-k', label='GMM fitting')

# Plot each gaussian component
for i in range(len(means)):
    pdf = gmm.weights_[i] * scipy.stats.norm(gmm.means_[i], np.sqrt(gmm.covariances_[i])).pdf(x)
    ax.plot(x, pdf, label=f'Gaussian component {i}'+f'\n{round(gmm.means_[i][0], 3)} ± {round(np.sqrt(gmm.covariances_[i][0][0]), 3)}'.format(i+1))

ax.legend()
plt.show()
plt.savefig("Global_836_0.5XRRM_step_size_fitting_manual_select_5.png"
            , dpi=300)

