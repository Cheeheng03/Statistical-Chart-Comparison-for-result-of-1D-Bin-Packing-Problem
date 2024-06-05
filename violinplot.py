import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Directory where the CSV files are stored
directory = '.'

# Define the problems, algorithms to plot, and colors for each algorithm
problems = ['Problem_1', 'Problem_2', 'Problem_3', 'Problem_4', 'Problem_5']
algorithms = ['ABC', 'BF', 'FFD', 'GA']
metrics = ['Time', 'Fitness', 'Wastage']  # Metrics to plot
title = ['Time', 'Number of Bins Used', 'Wastage']
colors = ['blue', 'green', 'red', 'purple']  # Colors for each algorithm
suptitles = ['TEST0049', 'TEST0014', 'TEST0082', 'TEST0044', 'TEST0030']

# Prepare violin plot for each problem
for problem, suptitle in zip(problems, suptitles):
    all_data = {metric: [] for metric in metrics}

    # Load the data for each algorithm
    for algo in algorithms:
        filename = f'{algo}_{problem}_Data.csv'
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            data = pd.read_csv(filepath)
            for metric in metrics:
                all_data[metric].append(data[metric])

    fig, axs = plt.subplots(1, 3, figsize=(10, 8), constrained_layout=True)
    fig.suptitle(suptitle)

    for i, metric in enumerate(metrics):
        parts = axs[i].violinplot(all_data[metric], showmeans=True)
        for pc, color in zip(parts['bodies'], colors):
            pc.set_facecolor(color)
            pc.set_edgecolor('black')

        axs[i].set_title(title[i])
        axs[i].set_xticks(np.arange(1, len(algorithms) + 1))
        axs[i].set_xticklabels(algorithms)
        axs[i].set_ylabel(title[i])

    plt.savefig(f'{directory}/{problem}_Violin_Plots.png', bbox_inches='tight')
    plt.show()
