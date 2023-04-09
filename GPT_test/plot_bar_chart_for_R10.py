import matplotlib.pyplot as plt
import numpy as np

# Define the data
set_1 = np.array([[12.5, 25], [1, 1]])
set_2 = np.array([[12.5, 25], [1, 0.977]])

# Define the labels for the x-axis ticks
x_labels = ['12.5 nM', '25 nM']

# Define the positions for the bars on the x-axis
x_pos = np.arange(len(x_labels))

# Define the width of each bar
bar_width = 0.1

# Plot the bars for set_1
plt.bar(x_pos - bar_width, set_1[1], bar_width, label='at 50 mM KCl')

# Plot the bars for set_2
plt.bar(x_pos, set_2[1], bar_width, label='at 150 mM KCl')

# Add x-axis labels and title
plt.xlabel('[Rec10] concentration')
plt.ylabel('Condensation efficiency')
plt.title('Condensation efficiency of Rec10')

# Add x-axis ticks and tick labels
plt.xticks(x_pos-bar_width/2, x_labels)

# Add a legend
# plt.legend(loc='upper right')
plt.legend()

# Show the plot
plt.show()
