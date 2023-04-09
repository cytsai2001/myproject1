import numpy as np
import pandas as pd
import ruptures as rpt
import matplotlib.pyplot as plt
import from_rupture_display
import pathlib


pd.options.mode.chained_assignment = None  # default='warn'


def main(path_to_parent_folder="/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/",
         path_excel="/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/2023-03-05-620lAa--fitresults_reshape_analyzed.xlsx",
         dead_time_start=29.40835,
         dead_time_end=45.19735,
         end_time=None):

    # Load the data
    df = pd.read_excel(path_excel, "BMx_fixing")

    # Call indexes of dead_time_start, dead_time_end
    index_dead_time_start = (df['time'] - dead_time_start).abs().idxmin()
    index_dead_time_end = (df['time'] - dead_time_end).abs().idxmin()

    # Filter out dead time period
    mask = (df["time"] >= df['time'][index_dead_time_start]) & (df["time"] <= df['time'][index_dead_time_end])
    for bead in range(df.shape[1] - 1):
        df.loc[mask, f"BMx_fixing_{bead}"] = 0

    # Filter out t > end_time if end_time
    if end_time:
        mask_end = (df["time"] >= df['time'][(df['time'] - end_time).abs().idxmin()])
        for bead in range(df.shape[1] - 1):
            df.loc[mask_end, f"BMx_fixing_{bead}"] = 0

    # Create two separate arrays for time values before and after the dead_time period
    before_dead_time = df[df["time"] < df['time'][index_dead_time_start]]
    after_dead_time = df[df["time"] > df['time'][index_dead_time_end]]

    # Create new folder in parent folder
    pathlib.Path(path_to_parent_folder + "/BMx_fixing_Pelt3000_mean_deadtime_2").mkdir(parents=True, exist_ok=False)

    # Create step.txt
    step_file = open(path_to_parent_folder + "/BMx_fixing_Pelt3000_mean_deadtime_2/step.txt", "w")

    for bead in range(after_dead_time.shape[1] - 1):
        try:
            # Replace NaN values with the last non-NaN value
            after_dead_time.loc[:, f"BMx_fixing_{bead}"].fillna(method='ffill', inplace=True)
        except KeyError:
            continue
        # Set values in "BM" column greater than 250 to zero
        after_dead_time.loc[:, f"BMx_fixing_{bead}"] = np.where(after_dead_time.loc[:, f"BMx_fixing_{bead}"] > 250, 0, after_dead_time.loc[:, f"BMx_fixing_{bead}"])

        # Apply change point analysis
        # # Way 1: If n_bkps is known
        # algo = rpt.Dynp(model="l1").fit(df[f"BMx_fixing_{bead}"].values)
        # my_bkps = algo.predict(n_bkps=8)
        # bkps_to_time = [df['time'][bkp_index] for bkp_index in my_bkps if bkp_index != 1500]
        # Way 2: If n_bkps is unknown
        algo = rpt.Pelt(model="l2").fit(after_dead_time[f"BMx_fixing_{bead}"].values)
        my_bkps = algo.predict(pen=3000)
        my_bkps += after_dead_time.index[0]
        bkps_to_time = [after_dead_time['time'][bkp_index] for bkp_index in my_bkps if bkp_index != (after_dead_time.index[-1] + 1)]
        if my_bkps[0] == (after_dead_time.index[-1] + 1):
            my_bkps[0] -= 1

        # Get the mean and std of each step
        means = [np.mean(before_dead_time[f"BMx_fixing_{bead}"].values)]
        stds = [np.std(before_dead_time[f"BMx_fixing_{bead}"].values)]
        init_start = 0
        first_end = index_dead_time_start
        first_step_data = df[f"BMx_fixing_{bead}"][init_start:first_end]

        second_start = index_dead_time_end
        second_end = my_bkps[0]
        second_step_data = df[f"BMx_fixing_{bead}"][second_start:second_end]
        means.append(second_step_data.mean())
        stds.append(second_step_data.std())
        for j in range(len(my_bkps) - 1):
            start = my_bkps[j]
            end = my_bkps[j + 1]
            step_data = df[f"BMx_fixing_{bead}"][start:end]
            means.append(step_data.mean())
            stds.append(step_data.std())

        # Print the results
        print(f"BMx_fixing_{bead}", file=step_file)
        print("Step {}: from time {} to {}, with BM = {} ± {}".format(
            0, df["time"][0], df["time"][index_dead_time_start], means[0], stds[0]
        ), file=step_file)

        print("Step {}: from time {} to {}, with BM = {} ± {}".format(
            1, df["time"][index_dead_time_end], df["time"][my_bkps[0]], means[1], stds[1]
        ), file=step_file)

        for i in range(len(my_bkps) - 1):
            print("Step {}: from time {} to {}, with BM = {} ± {}".format(
                i + 2, df["time"][my_bkps[i]], df["time"][my_bkps[i + 1] - 1], means[i + 2], stds[i + 2]
            ), file=step_file)

        # Plot results
        fig, ax = from_rupture_display.display(df[f"BMx_fixing_{bead}"], df['time'], bkps_to_time, layout='constrained')
        fig.supxlabel("Time (sec)")
        ax[0].set_xlim(0, 1000)
        fig.supylabel("BM (nm)")
        ax[0].set_ylim(0, 200)
        fig.suptitle(f"BMx_fixing_{bead}")

        # Add mean BM value and standard deviation area for each step
        try:
            if not pd.isnull(means[0]):
                start = 0
                end = df["time"][index_dead_time_start]
                time_range = np.arange(start, end, 0.02)
                ax[0].fill_between(time_range, means[0] - stds[0], means[0] + stds[0], facecolor='#595959', alpha=0.2)
                ax[0].plot(time_range, [means[0]] * len(time_range), linestyle='--', color='black')
        except IndexError:
            continue
        try:
            if not pd.isnull(means[1]):
                start = df["time"][index_dead_time_end]
                end = df["time"][my_bkps[0]]
                time_range = np.arange(start, end, 0.02)
                ax[0].fill_between(time_range, means[1] - stds[1], means[1] + stds[1], facecolor='#595959', alpha=0.2)
                ax[0].plot(time_range, [means[1]] * len(time_range), linestyle='--', color='black')
        except IndexError:
            continue
        try:
            for i in range(len(my_bkps) - 1):
                if not pd.isnull(means[i + 2]):
                    start = df["time"][my_bkps[i]]
                    end = df["time"][my_bkps[i + 1] - 1]
                    time_range = np.arange(start, end, 0.02)
                    ax[0].fill_between(time_range, means[i + 2] - stds[i + 2], means[i + 2] + stds[i + 2], facecolor='#595959', alpha=0.2)
                    ax[0].plot(time_range, [means[i + 2]] * len(time_range), linestyle='--', color='black')
        except IndexError:
            continue

        ax[0].axvspan(dead_time_start, dead_time_end, facecolor='#808080', alpha=1)
        plt.savefig(path_to_parent_folder + f"/BMx_fixing_Pelt3000_mean_deadtime_2/BMx_fixing_{bead}.png"
                    , dpi=300)
        plt.close()

#
# if __name__ == '__main__':
#     main("/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/",
#          "/Users/joytsai/Desktop/JoyTsai/Lab/Data/20230303/1-1-1162bp-50mMKCl-1.32uMRRM-rt/2023-03-05-620lAa--fitresults_reshape_analyzed.xlsx",
#          dead_time_start=29.40835, dead_time_end=45.19735)
