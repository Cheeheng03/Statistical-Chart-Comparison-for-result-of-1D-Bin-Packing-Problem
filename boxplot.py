import matplotlib.pyplot as plt
import pandas as pd
import os

# Directory where the CSV files are stored
directory = '.'

# Define the problems, algorithms to plot, and colors for each algorithm
problems = ['Problem_1', 'Problem_2', 'Problem_3', 'Problem_4', 'Problem_5']
algorithms = ['FFD', 'GA', 'SA', 'TABU']
metrics = ['Time', 'Fitness', 'Wastage']
titles = ['Time (ms)', 'Number of Bins Used', 'Wastage']
colors = ['blue', 'green', 'red', 'purple']
suptitles = ['TEST0049', 'TEST0014', 'TEST0082', 'TEST0044', 'TEST0030']

# Prepare box plot for each problem
for problem, suptitle in zip(problems, suptitles):
    all_data = {metric: [] for metric in metrics}
    stats = {metric: [] for metric in metrics}

    # Load the data for each algorithm
    for algo in algorithms:
        filename = f'{algo}_{problem}_Data.csv'
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            data = pd.read_csv(filepath)
            for metric in metrics:
                all_data[metric].append(data[metric])
                # Calculating and storing statistics
                stats[metric].append({
                    'max': data[metric].max(),
                    'median': data[metric].median(),
                    'min': data[metric].min()
                })

    # Printing stats in the terminal
    print(f"\n{problem} - {suptitle}")
    for metric in metrics:
        print(f"\n{metric}:")
        for algo, stat in zip(algorithms, stats[metric]):
            print(f"{algo} - Max: {stat['max']}, Median: {stat['median']}, Min: {stat['min']}")

    # Creating box plots
    fig, axs = plt.subplots(1, 3, figsize=(12, 8), constrained_layout=True)
    fig.suptitle(suptitle)

    for i, metric in enumerate(metrics):
        # Plotting
        axs[i].boxplot(all_data[metric], patch_artist=True,
                       boxprops=dict(facecolor=colors[i], color='black'),
                       medianprops=dict(color='yellow'),
                       whiskerprops=dict(color='black'),
                       capprops=dict(color='black'),
                       flierprops=dict(marker='o', color='black', markersize=5))
        # Setting titles and labels
        axs[i].set_title(titles[i])
        axs[i].set_xticks(range(1, len(algorithms) + 1))
        axs[i].set_xticklabels(algorithms)
        axs[i].set_ylabel(titles[i])

    # Saving and showing the figure
    plt.savefig(f'{directory}/{problem}_Box_Plots.png', bbox_inches='tight')
    plt.show()
