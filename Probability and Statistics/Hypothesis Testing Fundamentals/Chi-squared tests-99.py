## 2. Calculating differences ##

female_diff = (10771 - 16280.5) / 16280.5
print(female_diff)

male_diff = (21790 - 16280.5) / 16280.5
print(male_diff)

## 3. Updating the formula ##

female_diff = ((10771 - 16280.5) ** 2) / 16280.5
print(female_diff)

male_diff = ((21790 - 16280.5) ** 2) / 16280.5
print(male_diff)

gender_chisq = male_diff + female_diff
print(gender_chisq)

## 4. Generating a distribution ##

chi_squared_values = []
from numpy.random import random
import matplotlib.pyplot as plt

for x in range(0, 1000):
    randomnum = random((32561,))
    randomnum[randomnum < .5] = 0
    randomnum[randomnum >= .5] = 1
    male_count = len(randomnum[randomnum == 0])
    female_count = len(randomnum[randomnum == 1])
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)

    
    

## 6. Smaller samples ##

female_diff = (107.71 - 162.805) ** 2 / 162.805
print(female_diff)

male_diff = (217.90 - 162.805) ** 2 / 162.805
print(male_diff)

gender_chisq = male_diff + female_diff
print(gender_chisq)


## 7. Sampling distribution equality ##

chi_squared_values = []

from numpy.random import random
for x in range(1000):
    randomnum = random((300,))
    randomnum[randomnum < .5] = 0
    randomnum[randomnum >= .5] = 1
    male_count = len(randomnum[randomnum == 0])
    female_count = len(randomnum[randomnum == 1])
    male_diff = (male_count - 150) ** 2 / 150
    female_diff = (female_count - 150) ** 2 / 150
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)
    
plt.hist(chi_squared_values)
    

## 9. Increasing degrees of freedom ##

diffslst = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for idx, obs in enumerate(observed):
    exp = expected[idx]
    diff = ((obs - exp) ** 2) / exp
    diffslst.append(diff)
    
race_chisq = sum(diffslst)
print(race_chisq)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

observed = np.array([27816, 3124, 1039, 311, 271])
expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

chisquare_value, race_pvalue = chisquare(observed, expected)
print(chisquare_value)
print(race_pvalue)