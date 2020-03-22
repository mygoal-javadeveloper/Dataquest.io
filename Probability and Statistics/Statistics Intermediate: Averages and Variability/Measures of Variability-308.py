## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

def findrange(arr):
    return max(arr) - min(arr)

range_by_year={}
years = houses['Yr Sold'].unique()
print(years)
for yr in years:
    df = houses[houses['Yr Sold'] == yr]
    range_by_year[yr] = findrange(df['SalePrice'])
   
print(range_by_year)

one = False
print(one)
two = True
print(two)

## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

def avgdistance(arr):
    dist=[]
    meanval = sum(arr) / len(arr)
    print(meanval)
    for ele in arr:
        dist.append(ele - meanval)
    print(dist)    
    return sum(dist) / len(dist)
        
    
avg_distance = avgdistance(C)
print(avg_distance)


## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]

def mean_absolute_deviation(arr):
    meanabsdev= []
    meanval = sum(arr) / len(arr)
    for ele in arr:
        meanabsdev.append(abs(ele - meanval))
    print(meanval)
    print(meanabsdev)
    return sum(meanabsdev) / len(meanabsdev)

mad = mean_absolute_deviation(C)
print(mad)

        

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def meansquareddist(arr):
    meansqdist=[]
    meanval = sum(arr) / len(arr)
    for ele in arr:
        meansqdist.append((ele - meanval)**2)
    print(meanval)
    print(meansqdist)
    return sum(meansqdist) / len(meansqdist)

variance_C=meansquareddist(C)
print(variance_C)


## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def standard_deviation(arr):
    std_dev=[]
    meanval = sum(arr) / len(arr)
    for ele in arr:
        std_dev.append((ele-meanval)**2)
    print(meanval)
    print(std_dev)
    return sqrt(sum(std_dev) / len(std_dev))

standard_deviation_C = standard_deviation(C)
print(standard_deviation_C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    print(reference_point)
    print(variance)
    return sqrt(variance)

print(standard_deviation(houses['SalePrice']))

mean = houses['SalePrice'].mean()
st_dev = standard_deviation(houses['SalePrice'])
houses['SalePrice'].plot.hist()
plt.axvline(mean, color = 'Black', label = 'Mean')
plt.axvline(mean - st_dev, color = 'Red', label = 'Below')
plt.axvline(mean + st_dev, color = 'Violet', label = 'Above')
plt.legend()
plt.show()

years=houses['Yr Sold'].unique()
print(years)

variability={}
for yr in years:
    df = houses[houses['Yr Sold'] == yr]
    variability[yr] = standard_deviation(df['SalePrice'])
    
print(variability)

greatest_variability = max(variability, key=variability.get)
print(greatest_variability)
lowest_variability = min(variability, key=variability.get)
print(lowest_variability)

        
        

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

bigger_spread = 'sample 2'
print(bigger_spread)
st_dev1 = standard_deviation(sample1)
print(st_dev1)
st_dev2 = standard_deviation(sample2)
print(st_dev2)

## 8. The Sample Standard Deviation ##

import matplotlib.pyplot as plt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

std_devlst=[]
for x in range(5000):
    samplelst = houses['SalePrice'].sample(10, random_state=x)
    std_devlst.append(standard_deviation(samplelst))

#(std_devlst)
plt.hist(std_devlst)
#plt.axvline(houses['SalePrice'].std())
plt.axvline(standard_deviation(houses['SalePrice']))
plt.show()

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances) -1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

plt.hist(st_devs)
plt.axvline(pop_stdev)  # pop_stdev is pre-saved from the last screen
plt.show()

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var
pandas_stdev = sample['SalePrice'].std(ddof = 1)
print(pandas_stdev)
numpy_stdev = std(sample['SalePrice'], ddof = 1)
print(numpy_stdev)
equal_stdevs = pandas_stdev == numpy_stdev
print(equal_stdevs)
pandas_var = sample['SalePrice'].var(ddof = 1)
print(pandas_var)
numpy_var = var(sample['SalePrice'], ddof = 1)
print(numpy_var)
equal_vars = pandas_var == numpy_var
print(equal_vars)

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

from numpy import std, var
samplestd=[]
samplevar=[]
for smpl in samples:
    samplestd.append(std(smpl, ddof = 1))
    samplevar.append(std(smpl, ddof = 1))
    
equal_stdev = (sum(samplestd) / len(samplestd)) == std(population, ddof=0)
equal_var = (sum(samplevar) / len(samplevar)) == var(population , ddof=0)
print(equal_stdev)
print(equal_var)