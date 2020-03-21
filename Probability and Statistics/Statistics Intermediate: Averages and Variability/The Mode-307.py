## 1. Introduction ##

import pandas as pd
houses=pd.read_table('AmesHousing_1.txt')
print(houses['Land Slope'].value_counts())
scale_land='ordinal'
print(scale_land)
print(houses['Roof Style'].value_counts())
scale_roof='nominal'
print(scale_roof)
print(houses['Kitchen AbvGr'].value_counts())
kitchen_variable='discrete'
print(kitchen_variable)

## 2. The Mode for Ordinal Variables ##

landslopedict={}
def frequncy(arr):
    for x in arr:
        if x in landslopedict:
            landslopedict[x]+=1
        else:
            landslopedict[x]=1
    return max(landslopedict, key=landslopedict.get)

mode_function = frequncy(houses['Land Slope'])            
print(landslopedict)
print(mode_function)
mode_method = houses['Land Slope'].mode()
print(mode_method)
same = mode_function == mode_method
print(same)

## 3. The Mode for Nominal Variables ##

# The function we wrote (you can copy-paste yours from the previous screen)
def mode(array):
    counts = {}
    
    for value in array:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return max(counts, key = counts.get) , counts

mode , value_counts = mode(houses['Roof Style'])
print(mode)
print(value_counts)
print(houses['Roof Style'].value_counts())

## 4. The Mode for Discrete Variables ##

print(houses['Bedroom AbvGr'].value_counts())
bedroom_variable='discrete'
print(bedroom_variable)
bedroom_mode=houses['Bedroom AbvGr'].mode()
print(bedroom_mode)
print(houses['SalePrice'].value_counts())
price_variable='continuous'
print(price_variable)


## 5. Special Cases ##

intervals = pd.interval_range(start = 0, end = 800000, freq = 100000)
gr_freq_table = pd.Series([0,0,0,0,0,0,0,0], index = intervals)

for value in houses['SalePrice']:
    for interval in intervals:
        if value in interval:
            gr_freq_table.loc[interval] += 1
            break

print(gr_freq_table)
print(gr_freq_table.max())
print(gr_freq_table.idxmax())
mode=gr_freq_table.idxmax().mid
print(mode)
mean = houses['SalePrice'].mean()
print(mean)
median = houses['SalePrice'].median()
print(median)
sentence_1 = True
print(sentence_1)
sentence_2 = True
print(sentence_2)

## 6. Skewed Distributions ##

distribution_1 = {'mean': 3021 , 'median': 3001, 'mode': 2947}
distribution_2 = {'median': 924 , 'mode': 832, 'mean': 962}
distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

houses['SalePrice'].plot.kde(xlim = (houses['SalePrice'].min(),
                                     houses['SalePrice'].max()
                                    )
                            )
plt.axvline(150000, color = 'Green', label = 'Mode')
plt.axvline(houses['SalePrice'].median(), color = 'red', label = 'Median')
plt.axvline(houses['SalePrice'].mean(), color = 'Orange', label = 'Mean')
plt.legend()

shape_1 = 'right skew'
print(shape_1)
shape_2 = 'right skew'
print(shape_2)
shape_3 = 'left skew'
print(shape_3)

## 7. Symmetrical Distributions ##

import matplotlib.pyplot as plt
houses['Mo Sold'].plot.kde(xlim = [1,12])
print(houses['Mo Sold'].mode()[0])
plt.axvline(houses['Mo Sold'].mode()[0], color='green',label='Mode', linewidth =2)
plt.axvline(houses['Mo Sold'].median(), color='orange',label='Median', linewidth =2)
plt.axvline(houses['Mo Sold'].mean(), color='black',label='Mean',linewidth =2)
plt.legend()
plt.show()