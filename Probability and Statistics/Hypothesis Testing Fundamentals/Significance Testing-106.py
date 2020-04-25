## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

## 4. Test statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences = []

for x in range(0, 1000):
    group_a = []
    group_b = []
    for y in all_values:
        num = np.random.rand()
        if num >= 0.5:
            group_a.append(y)
        else:
            group_b.append(y)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)      
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()


## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for x in mean_differences:
    if sampling_distribution.get(x, False):
        val = sampling_distribution.get(x)
        sampling_distribution[x] = val+ 1
    else:
        sampling_distribution[x] = 1
        
print(sampling_distribution)

## 8. P value ##

frequencies = []
for keys, vals in sampling_distribution.items():
    if keys >= 2.52:
        frequencies.append(vals)


p_value = np.sum(frequencies) / 1000
print(p_value)