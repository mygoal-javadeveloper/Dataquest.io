## 1. Individual Values ##

import pandas as pd
import matplotlib.pyplot as plt
houses = pd.read_table('AmesHousing_1.txt')
houses['SalePrice'].plot.kde(xlim=(houses['SalePrice'].min(), houses['SalePrice'].max()))
plt.axvline(houses['SalePrice'].mean(), color='black', label='Mean')
plt.axvline(houses['SalePrice'].mean()+houses['SalePrice'].std(ddof=0), color='red', label='Standard deviation')
plt.axvline(220000, color='orange', label='220000')
plt.legend()
plt.show()
very_expensive = False
print(very_expensive)

## 2. Number of Standard Deviations ##

st_devs_away = (220000 - houses['SalePrice'].mean()) / houses['SalePrice'].std(ddof=0)
print(st_devs_away)
print('Yes it matches')


## 3. Z-scores ##

import numpy as np
min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def zscores(val, arr, bessel = 0):
    z = (val - arr.mean()) / np.std(arr, ddof = bessel)
    return z
min_z = zscores(min_val, houses['SalePrice'])
print(min_z)
mean_z = zscores(mean_val, houses['SalePrice'])
print(mean_z)
max_z = zscores(max_val, houses['SalePrice'])
print(max_z)

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

n_ames= z_score(value = 200000, array = houses[houses['Neighborhood'] == 'NAmes']['SalePrice'])
print(n_ames)
collgcr= z_score(value = 200000, array = houses[houses['Neighborhood'] == 'CollgCr']['SalePrice'])
print(collgcr)
oldtown= z_score(value = 200000, array = houses[houses['Neighborhood'] == 'OldTown']['SalePrice'])
print(oldtown)
edwards= z_score(value = 200000, array = houses[houses['Neighborhood'] == 'Edwards']['SalePrice'])
print(edwards)
somerst= z_score(value = 200000, array = houses[houses['Neighborhood'] == 'Somerst']['SalePrice'])
print(somerst)
best_investment = 'College Creek'
print(best_investment)

## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

plt.figure(figsize = (11,3.5))
plt.subplot(1,2,1)
houses['z_prices'].plot.kde(xlim = (houses['z_prices'].min(),
                                houses['z_prices'].max()
                                )
                        )
plt.subplot(1,2,2)
houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(),
                                    houses['SalePrice'].max()
                                     )
                            )
plt.tight_layout() # otherwise the plots will overlay partiallys

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof = 0)
    
print(z_mean_price)
print(z_stdev_price)

mean_area = houses['Lot Area'].mean()
print(mean_area)
stdev_area = houses['Lot Area'].std(ddof = 0)
print(stdev_area)
houses['z_area'] = houses['Lot Area'].apply(
    lambda x: ((x - mean_area) / stdev_area)
    )
z_mean_area = houses['z_area'].mean()
print(z_mean_area)
z_stdev_area = houses['z_area'].std(ddof = 0)
print(z_stdev_area)


## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

def meanstd(arr):
    meanarr = mean(arr)
    stdarr = std(arr, ddof = 0)
    lst = [] 
    for x in arr:
        lst.append((x-meanarr) / stdarr)
    return (mean(lst), std(lst, ddof = 0))
                   
mean_z, stdev_z = meanstd(population)
print(mean_z)
print(stdev_z)
                   
                   

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
print(standardized_sample)
print(mean(standardized_sample))
#print(std(standardized_sample)) # ddof = 0 by default
stdev_sample = std(standardized_sample, ddof = 1)
print(stdev_sample)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)
houses['z_index1'] = houses['index_1'].apply(lambda x : (x - mean_index1) / stdev_index1)

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)
houses['z_index2'] = houses['index_2'].apply(lambda x : (x - mean_index2) / stdev_index2)

print(houses[['z_index1', 'z_index2']].head(2))
better = 'first'
print(better)


## 9. Converting Back from Z-scores ##

meanpop = 50
stddevpop = 10
houses['transformed'] = houses['z_merged'].apply(lambda x : (x * stddevpop + meanpop))
print(houses['transformed'])
mean_transformed = houses['transformed'].mean()
print(mean_transformed)
stdev_transformed = houses['transformed'].std(ddof = 0)
print(stdev_transformed)