import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example data for each algorithm
data = {
    'Algorithm': ['ABC', 'BF', 'FFD', 'GA'],
    'Average Time (ms)': [692.82, 0.26, 0.20, 3099.74],
    'Average Bins Used': [20.70, 20.70, 20.80, 20.44],
    'Average Wastage': [9126.40, 9066.40, 10086.40, 6446.40]
}

df = pd.DataFrame(data)

# Normalize each metric
max_time = df['Average Time (ms)'].max()
max_bins = df['Average Bins Used'].max()
max_wastage = df['Average Wastage'].max()

df['Average Time'] = df['Average Time (ms)'] / max_time
df['Average Bins Used'] = df['Average Bins Used'] / max_bins
df['Average Wastage'] = df['Average Wastage'] / max_wastage

# Plotting the radar chart
labels = np.array(['Average Time', 'Average Bins Used', 'Average Wastage'])
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Set font sizes
plt.rcParams.update({'font.size': 20})  # Adjust this value as needed

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Color palette: Vivid and distinguishable
colors = ['darkorange', 'darkgreen', 'navy', 'magenta']

for i, row in df.iterrows():
    values = row[['Average Time', 'Average Bins Used', 'Average Wastage']].tolist()
    values += values[:1]
    ax.fill(angles, values, alpha=0.25, label=row['Algorithm'], color=colors[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()
