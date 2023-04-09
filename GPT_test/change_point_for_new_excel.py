import numpy as np
import pandas as pd
import ruptures as rpt
import matplotlib.pyplot as plt
import from_rupture_display
import pathlib
plt.ioff()

df = pd.read_excel("/Users/joytsai/Downloads/20230113/3-2-1162bp-150mMKCl-25nMRec10-rt/2023-01-30-064qRg--fitresults_reshape_analyzed.xlsx"
                   , "BMy_fixing", header=1, index_col=0)
df.reset_index(drop=False, inplace=True)
column_name = ['time']
for col in range(df.shape[1] - 1):
    column_name.append(f"BMy_fixing_{col}")
df.columns = column_name

# Create new folder in parent folder
pathlib.Path("/Users/joytsai/Downloads/20230113/3-2-1162bp-150mMKCl-25nMRec10-rt/BMy_fixing_Pelt").mkdir(parents=True, exist_ok=False)

# Create step.txt
step_file = open("/Users/joytsai/Downloads/20230113/3-2-1162bp-150mMKCl-25nMRec10-rt/BMy_fixing_Pelt/step.txt", "w")

for bead in range(df.shape[1] - 1):
    try:
        # Replace NaN values with the last non-NaN value
        df[f"BMy_fixing_{bead}"].fillna(method='ffill', inplace=True)
    except KeyError:
        continue

    # Set values in "BM" column greater than 250 to zero
    df[f"BMy_fixing_{bead}"] = np.where(df[f"BMy_fixing_{bead}"] > 250, 0, df[f"BMy_fixing_{bead}"])

    # Apply change point analysis
    # # Way 1: If n_bkps is known
    # algo = rpt.Dynp(model="l1").fit(df[f"BMx_fixing_{bead}"].values)
    # my_bkps = algo.predict(n_bkps=8)
    # bkps_to_time = [df['time'][bkp_index] for bkp_index in my_bkps if bkp_index != 1500]
    # Way 2: If n_bkps is unknown
    algo = rpt.Pelt(model="l2").fit(df[f"BMy_fixing_{bead}"].values)
    my_bkps = algo.predict(pen=2000)
    bkps_to_time = [df['time'][bkp_index] for bkp_index in my_bkps if bkp_index != df.shape[0]]
    if my_bkps[0] == df.shape[0]:
        my_bkps[0] -= 1

    # Get the mean and std of each step
    means = []
    stds = []
    init_start = 0
    first_end = my_bkps[0]
    first_step_data = df[f"BMy_fixing_{bead}"][init_start:first_end]
    means.append(first_step_data.mean())
    stds.append(first_step_data.std())
    for j in range(len(my_bkps) - 1):
        start = my_bkps[j]
        end = my_bkps[j + 1]
        step_data = df[f"BMy_fixing_{bead}"][start:end]
        means.append(step_data.mean())
        stds.append(step_data.std())

    # Print the results
    print(f"BMy_fixing_{bead}", file=step_file)
    print("Step {}: from time {} to {}, with BM = {} ± {}".format(
        0, df["time"][0], df["time"][my_bkps[0]], means[0], stds[0]
    ), file=step_file)
    for i in range(len(my_bkps) - 1):
        print("Step {}: from time {} to {}, with BM = {} ± {}".format(
            i + 1, df["time"][my_bkps[i]], df["time"][my_bkps[i + 1] - 1], means[i + 1], stds[i + 1]
        ), file=step_file)

    # Plot results
    fig, ax = from_rupture_display.display(df[f"BMy_fixing_{bead}"], df['time'], bkps_to_time, layout='constrained')
    fig.supxlabel("Time (sec)")
    ax[0].set_xlim(0, 1000)
    fig.supylabel("BM (nm)")
    ax[0].set_ylim(0, 150)
    fig.suptitle(f"BMy_fixing_{bead}")
    plt.savefig(f"/Users/joytsai/Downloads/20230113/3-2-1162bp-150mMKCl-25nMRec10-rt/BMy_fixing_Pelt/BMy_fixing_{bead}.png"
                , dpi=300)
    plt.close()

step_file.close()
