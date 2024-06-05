import pandas as pd
import os

# Directory containing the CSV files
directory = '.'

# Algorithms and their corresponding data files
algorithms = {
    'ABC': 'ABC_Problem_{}_Data.csv',
    'BF': 'BF_Problem_{}_Data.csv',
    'FFD': 'FFD_Problem_{}_Data.csv',
    'GA': 'GA_Problem_{}_Data.csv'
}

# Data storage for averages
average_results = {}

# Process each algorithm's data files
for algo, filename_pattern in algorithms.items():
    times = []
    bins_used = []
    wastages = []

    # Loop over each of the 5 problem data files
    for i in range(1, 6):
        filepath = os.path.join(directory, filename_pattern.format(i))
        if os.path.exists(filepath):
            data = pd.read_csv(filepath)

            # Assume the columns are named 'Time', 'Bins Used', and 'Wastage'
            # Adjust these as necessary to match your actual column names
            times.append(data['Time'].mean())
            bins_used.append(data['Fitness'].mean())  # Make sure to use the correct column name
            wastages.append(data['Wastage'].mean())

    # Calculate average for each metric
    average_time = sum(times) / len(times)
    average_bins_used = sum(bins_used) / len(bins_used)
    average_wastage = sum(wastages) / len(wastages)

    # Store in results
    average_results[algo] = {
        'AverageTime': average_time,
        'AverageNumberOfBinsUsed': average_bins_used,
        'AverageWastage': average_wastage
    }

# Output the results
for algo, metrics in average_results.items():
    print(f"{algo}:")
    print(f" Average Time: {metrics['AverageTime']:.2f} ms")
    print(f" Average Number of Bins Used: {metrics['AverageNumberOfBinsUsed']:.2f}")
    print(f" Average Wastage: {metrics['AverageWastage']:.2f}")
    print("------")
