## 1. Introduction ##

mean_new=houses_per_year['Mean Price'].mean()
mean_original=houses['SalePrice'].mean()
difference=mean_original - mean_new
print(difference)

## 2. Different Weights ##

weighted_mean=round(sum(houses_per_year['Mean Price']*houses_per_year['Houses Sold']) / sum(houses_per_year['Houses Sold']),10)
print(weighted_mean)
mean_original=round((houses['SalePrice'].mean()),10)
print(mean_original)
difference = mean_original - weighted_mean
print(difference)

    

## 3. The Weighted Mean ##

import numpy as np
def calculate_weightedmean(meanval, weightval):
    return round(sum(meanval * weightval) / sum(weightval),10)

weighted_mean_function = calculate_weightedmean(houses_per_year['Mean Price'],houses_per_year['Houses Sold'])
weighted_mean_numpy = round(np.average(a=houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold']),10)
equal = weighted_mean_function == weighted_mean_numpy
print(weighted_mean_function)
print(weighted_mean_numpy)
print(equal)


## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1=23
print(median1)
median2=55
print(median2)
median3=32
print(median3)

distribution4=[3,7,2,12]
distribution4.sort()
print(distribution4)
median4= (7+3)/2
print(median4)

## 5. Distributions with Even Number of Values ##

totrms_abvgrd = houses['TotRms AbvGrd'].copy()
totrms_abvgrd = totrms_abvgrd.replace('10 or more' , 10).astype(int)
print(type(totrms_abvgrd))
totrms_abvgrd = totrms_abvgrd.sort_values()
print(len(totrms_abvgrd))
middle_indices = [int((len(totrms_abvgrd) / 2) - 1),
                  int((len(totrms_abvgrd) / 2))
                 ] # len - 1 and len because Series use 0-indexing 
print(middle_indices)
median = totrms_abvgrd.iloc[middle_indices].mean()
print(median)

## 6. The Median as a Resistant Statistic ##

import matplotlib.pyplot as plt
houses['Lot Area'].plot.box()
plt.show()
houses['SalePrice'].plot.box()
plt.show()
lotarea_difference = houses['Lot Area'].mean() - houses['Lot Area'].median()
print(lotarea_difference)
saleprice_difference = houses['SalePrice'].mean() - houses['SalePrice'].median()
print(saleprice_difference)

## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median = houses['Overall Cond'].median()
print(mean)
print(median)
houses['Overall Cond'].plot.hist()
more_representative = 'mean'
print(more_representative)