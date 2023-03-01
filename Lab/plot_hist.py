import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy.stats import norm


data_to_plot_before = np.array([99.305505, 112.3062345, 121.8220751, 97.05416589, 96.27757021, 97.34658368, 97.16159677,
                                91.24476039, 121.2116723, 102.9808864, 101.9052721, 102.3526126, 92.07673957, 97.20167479,
                                108.1500555, 100.1790202, 113.0364112, 119.3241099, 82.25106486, 107.0414538, 92.277596,
                                213.7278569, 49.32358237, 91.90640569, 100.141557, 73.07874668, 103.3518635, 100.4268738,
                                56.88729928, 101.7314075, 89.43609453, 136.2983809, 75.54572757, 124.8339253, 98.72165537,
                                95.05963001, 98.44760229, 99.19072286, 101.0900929, 104.0243461, 100.434665, 105.1258953,
                                122.790025, 95.4003061])


data_to_plot_after = np.array([3.672963275, 4.227632482, 7.992311494, 67.78209834, 4.089956008, 3.843165833, 79.73281432,
                               5.178363433, 4.174864274, 56.85967909, 26.60269411, 66.55174642, 53.25751713, 3.669296375,
                               3.839218363, 4.087234788, 4.056651529, 4.727287999, 36.33177486, 30.15793447, 59.05436676,
                               37.75899971, 10.87993967, 41.56954159, 5.757082096, 59.12856701, 3.089150305, 11.73002575,
                               4.331470441, 43.01470861, 2.587989529, 28.14326668, 50.35482181, 80.1018073, 8.285596648,
                               39.92845967, 50.04260818, 63.84263153, 2.889590049, 3.353849604, 5.610344814, 5.131821003,
                               13.70635056,	2.849898819])

data_after_remove_stuck = np.array([int(i) for i in data_to_plot_after if i >= 10])


plt.rc('ytick', labelsize=6)
fig, axs = plt.subplots(2, 1, sharex=True)
fig.subplots_adjust(hspace=0)
for nn, ax in enumerate(axs.flat):
    if nn == 0:
        (mu, sigma) = norm.fit(data_to_plot_before)
        n, bins, patches = ax.hist(data_to_plot_before, bins=30, range=(0, 150), density=True, color='black', edgecolor='white')
        ax.plot(bins, norm.pdf(bins, mu, sigma), 'r--', linewidth=2)
        ax.tick_params('x', labelbottom=False)
        ax.tick_params('y', rotation=50)
        ax.text(20, 0.047, 'Before Rec10', fontsize=10)
        ax.text(20, 0.04, f'N={len(data_to_plot_before)}')
        ax.text(20, 0.033, f'{round(mu, 3)} ± {round(sigma, 3)} (mean ± sd)')
    elif nn == 1:
        (mu, sigma) = norm.fit(data_after_remove_stuck)
        n, bins, patches = ax.hist(data_to_plot_after, bins=30, range=(0, 150), density=True, color='black', edgecolor='white')
        ax.plot(bins, norm.pdf(bins, mu, sigma), 'r--', linewidth=2)
        ax.tick_params('x')
        ax.tick_params('y', rotation=50)
        ax.text(20, 0.065, '15 min after Rec10 incubation (same FOV)', fontsize=10)
        ax.text(20, 0.055, f'N={len(data_to_plot_before)} (N_fit={len(data_after_remove_stuck)}, stuck bead (BM <= 10) excluded)')
        ax.text(20, 0.045, f'{round(mu, 3)} ± {round(sigma, 3)} (mean ± sd)')

fig.suptitle('25 nM Rec20; 150 mM KCl; 1162 bp dsDNA', y=0.95)
fig.supylabel('Probability density', x=0.05)
fig.supxlabel('BM (nm)')
plt.savefig('hist_before_after.png', dpi=300)

