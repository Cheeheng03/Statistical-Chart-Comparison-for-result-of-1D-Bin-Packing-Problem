import matplotlib.pyplot as plt
import pandas as pd

# Data preparation (example data)
data = pd.DataFrame({
    'Algorithm': ['ABC', 'BF', 'FFD', 'GA'],
    'Time': [21, 0, 0, 2261],  # Best times for a problem
    'Fitness': [28, 28, 28, 28],  # Best fitness for a problem
    'Wastage': [10035, 10035, 10035, 10035]  # Lowest wastage for a problem
})

# Colors for the bars
colors = ['red', 'yellow', 'blue', 'green']

# Plot setup
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Performance Comparison of Algorithms - TEST0030', fontsize=16)

# Time subplot
time_sorted = data.sort_values('Time', ascending=True)
axs[0].bar(time_sorted['Algorithm'], time_sorted['Time'], color=colors)
axs[0].set_title('Best Time Comparison')
axs[0].set_ylabel('Time')

# Fitness subplot
fitness_sorted = data.sort_values('Fitness', ascending=False)
axs[1].bar(fitness_sorted['Algorithm'], fitness_sorted['Fitness'], color=colors)
axs[1].set_title('Best Fitness Comparison')
axs[1].set_ylabel('Fitness')

# Wastage subplot
wastage_sorted = data.sort_values('Wastage', ascending=True)
axs[2].bar(wastage_sorted['Algorithm'], wastage_sorted['Wastage'], color=colors)
axs[2].set_title('Best Wastage Comparison')
axs[2].set_ylabel('Wastage')

# Layout and save
plt.tight_layout()
plt.subplots_adjust(top=0.88)  # Adjust top to accommodate for suptitle

# Save the figure to the specified directory
plt.savefig('Performance_Comparison_TEST0030.png')

# You can display the plot if you want, or close to avoid showing it during a script run
# plt.show()
plt.close()
