# generar una normal de altura y peso
import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))

print(np_city)

# Print mean height (first column)
avg = round(np.mean(np_city[:,0]),2)
print("Average: " + str(avg))

# Print median height.
med = np.median(np_city[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height.
stddev = round(np.std(np_city[:,0]),2)
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column.
corr = np.corrcoef(np_city[:,0],np_city[:,1])
print("Correlation: " + str(corr))