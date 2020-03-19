## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
mean = sum(distribution) / len(distribution)
print(mean)
centernum = sum(range(0, 14))/13
print(centernum)
center = centernum == mean
print(center)
abovemean = []
belowmean = []
for x in distribution:
    if x < mean:
        belowmean.append(mean-x)
    elif x > mean:
        abovemean.append(x-mean)
equal_distances = sum(belowmean) == sum(abovemean)
print(equal_distances)

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
distlst=[]
equal_distances = 0
for x in range(0, 5000):
    seed(x)
    distlst.append(list(randint(low=0, high=1000, size=10)))
    
for lst in distlst: 
    mean = sum(lst)/len(lst)
    abovemean=[]
    belowmean=[]
    for ls in lst:
        if ls == mean:
            continue
        elif ls > mean:
            abovemean.append(ls - mean)
        elif ls < mean:
            belowmean.append(mean-ls)
    if((round(sum(abovemean),1)) == (round(sum(belowmean),1))):
        equal_distances+=1
print(equal_distances)

    
    

## 4. Defining the Mean Algebraically ##

#We use the mew symbol  to denote both the population and the sample mean. Assign #True or False to a variable named one.
one=False 
print(one)
#If a population has 8 values, then n=8 . Assign True or False to a variable #named two.
two=False
print(False)
#x bar is a symbol used as an alternative to M , X bar, or x bar n  to denote # the population mean. Assign True or False to a variable named three.
three=False
print(False)

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def populationmean(lst):
    sum_distribution=0
    for val in lst:
        sum_distribution+=val
    return sum_distribution / len(lst)

mean_1 = populationmean(distribution_1)
print(mean_1)
mean_2 = populationmean(distribution_2)
print(mean_2)
mean_3 = populationmean(distribution_3)
print(mean_3)

## 6. Introducing the Data ##

import pandas as pd
houses=pd.read_table('AmesHousing_1.txt')
print(houses.shape)
one=True
print(one)
#print(houses['SalePrice'].value_counts().sort_index())
two=False
print(two)
three=True
print(three)


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
    return sum_distribution / len(distribution)

print(houses['SalePrice'].describe())
print(houses['SalePrice'].value_counts())

function_mean = mean(houses['SalePrice'])
print(function_mean)
pandas_mean = houses['SalePrice'].mean()
print(pandas_mean)
means_are_equal = function_mean == pandas_mean
print(means_are_equal)


## 8. Estimating the Population Mean ##

import matplotlib.pyplot as plt
def calculate_samplemean(lst):
    sample_mean = {}
    sample_size = 5
    for i in range(0,101):
        samplelst = lst.sample(n=sample_size, random_state=i)
        samplemean = sum(samplelst) / len(samplelst)
        sample_mean[sample_size] = samplemean
        sample_size+=29
    return sample_mean   
 
samplingsmean=calculate_samplemean(houses['SalePrice'])
samplingssize=sorted(samplingsmean.keys())
samplingserror=[]
parameter=houses['SalePrice'].mean()
for x in sorted(samplingsmean.keys()):
    samplingserror.append(parameter - samplingsmean[x])
    
plt.scatter(x=samplingssize, y=samplingserror)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')
plt.show()
    
    


## 9. Estimates from Low-Sized Samples ##

import matplotlib.pyplot as plt
def sample_mean(lst):
    sampling_mean = []
    for x in range(10000):
        sampling_mean.append(lst.sample(n=100, random_state=x).mean())
    return sampling_mean

samplingmean=sample_mean(houses['SalePrice'])
plt.hist(samplingmean)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel('Sample mean')
plt.ylabel('Frequency')
plt.xlim(0,500000)
plt.show()

print('yes')

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

samples=[[3,7],[3,2],
         [7,2],[7,3],
         [2,3],[2,7]
        ]
sample_means=[]
for lst in samples:
    sample_means.append(sum(lst)/len(lst))
    
unbiased = ((sum(sample_means)/len(sample_means)) == (sum(population)/len(population)))

print(unbiased)