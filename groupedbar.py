import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Directory where the CSV files are stored
directory = '.'

# Define the specific problems and their titles
problems = ['Problem_2', 'Problem_3', 'Problem_5']
titles = ['Time for TEST0014', 'Time for TEST0082', 'Time for TEST0030']
algorithms = ['ABC', 'BF', 'FFD', 'GA']
colors = ['blue', 'green', 'red', 'purple']  # Colors for each algorithm

# Prepare a single figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(10, 8), constrained_layout=True)


# Load and plot the data for each selected problem
for ax, problem, title in zip(axs, problems, titles):
    all_data = []

    # Load the data for each algorithm
    for algo in algorithms:
        filename = f'{algo}_{problem}_Data.csv'
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            data = pd.read_csv(filepath)
            all_data.append(data['Time'])  # Append only 'Time' data

    # Create a violin plot for the 'Time' metric
    parts = ax.violinplot(all_data, showmeans=True)
    for pc, color in zip(parts['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_edgecolor('black')

    ax.set_title(title)
    ax.set_xticks(np.arange(1, len(algorithms) + 1))
    ax.set_xticklabels(algorithms)
    ax.set_ylabel('Time')

# Save the combined plot as a single image file
plt.savefig(f'{directory}/Combined_Time_Violin_Plots.png', bbox_inches='tight')
plt.show()
