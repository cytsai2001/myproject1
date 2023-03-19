import numpy as np
import pandas as pd
import ruptures as rpt
import matplotlib.pyplot as plt
import from_rupture_display
import pathlib


def main(path_to_parent_folder, path_excel):
    plt.ioff()

    # Load the data
    df = pd.read_excel(path_excel
                       , "BMx_fixing")

    # Create new folder in parent folder
    pathlib.Path(path_to_parent_folder + "/BMx_fixing_Pelt3000_mean").mkdir(parents=True, exist_ok=False)

    # Create step.txt
    step_file = open(path_to_parent_folder + "/BMx_fixing_Pelt3000_mean/step.txt", "w")

    for bead in range(df.shape[1] - 1):
        try:
            # Replace NaN values with the last non-NaN value
            df[f"BMx_fixing_{bead}"].fillna(method='ffill', inplace=True)
        except KeyError:
            continue

        # Set values in "BM" column greater than 250 to zero
        df[f"BMx_fixing_{bead}"] = np.where(df[f"BMx_fixing_{bead}"] > 250, 0, df[f"BMx_fixing_{bead}"])

        # Apply change point analysis
        # # Way 1: If n_bkps is known
        # algo = rpt.Dynp(model="l1").fit(df[f"BMx_fixing_{bead}"].values)
        # my_bkps = algo.predict(n_bkps=8)
        # bkps_to_time = [df['time'][bkp_index] for bkp_index in my_bkps if bkp_index != 1500]
        # Way 2: If n_bkps is unknown
        algo = rpt.Pelt(model="l2").fit(df[f"BMx_fixing_{bead}"].values)
        my_bkps = algo.predict(pen=3000)
        bkps_to_time = [df['time'][bkp_index] for bkp_index in my_bkps if bkp_index != df.shape[0]]
        if my_bkps[0] == df.shape[0]:
            my_bkps[0] -= 1

        # Get the mean and std of each step
        means = []
        stds = []
        init_start = 0
        first_end = my_bkps[0]
        first_step_data = df[f"BMx_fixing_{bead}"][init_start:first_end]
        means.append(first_step_data.mean())
        stds.append(first_step_data.std())
        for j in range(len(my_bkps) - 1):
            start = my_bkps[j]
            end = my_bkps[j + 1]
            step_data = df[f"BMx_fixing_{bead}"][start:end]
            means.append(step_data.mean())
            stds.append(step_data.std())

        # Print the results
        print(f"BMx_fixing_{bead}", file=step_file)
        print("Step {}: from time {} to {}, with BM = {} ± {}".format(
            0, df["time"][0], df["time"][my_bkps[0]], means[0], stds[0]
        ), file=step_file)
        for i in range(len(my_bkps) - 1):
            print("Step {}: from time {} to {}, with BM = {} ± {}".format(
                i + 1, df["time"][my_bkps[i]], df["time"][my_bkps[i + 1] - 1], means[i + 1], stds[i + 1]
            ), file=step_file)

        # Plot results
        fig, ax = from_rupture_display.display(df[f"BMx_fixing_{bead}"], df['time'], bkps_to_time, layout='constrained')
        fig.supxlabel("Time (sec)")
        ax[0].set_xlim(0, 1000)
        fig.supylabel("BM (nm)")
        ax[0].set_ylim(0, 200)
        fig.suptitle(f"BMx_fixing_{bead}")

        # Add mean BM value and standard deviation area for each step
        if not pd.isnull(means[0]):
            start = 0
            end = df["time"][my_bkps[0] - 1]
            time_range = np.arange(start, end, 0.02)
            ax[0].fill_between(time_range, means[0] - stds[0], means[0] + stds[0], facecolor='#595959', alpha=0.2)
            ax[0].plot(time_range, [means[0]] * len(time_range), linestyle='--', color='black')
        for i in range(len(my_bkps) - 1):
            if not pd.isnull(means[i + 1]):
                start = df["time"][my_bkps[i]]
                end = df["time"][my_bkps[i + 1] - 1]
                time_range = np.arange(start, end, 0.02)
                ax[0].fill_between(time_range, means[i + 1] - stds[i + 1], means[i + 1] + stds[i + 1], facecolor='#595959', alpha=0.2)
                ax[0].plot(time_range, [means[i + 1]] * len(time_range), linestyle='--', color='black')

        plt.savefig(path_to_parent_folder + f"/BMx_fixing_Pelt3000_mean/BMx_fixing_{bead}.png"
                    , dpi=300)
        plt.close()

# TODO: Dead time
