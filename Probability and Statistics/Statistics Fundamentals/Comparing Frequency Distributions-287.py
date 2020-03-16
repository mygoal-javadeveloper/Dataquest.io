## 2. Grouped Bar Plots ##

import seaborn as sns
sns.countplot(x='Exp_ordinal', hue='Pos', data=wnba, order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'], hue_order = ['C', 'F', 'F/C', 'G', 'G/F'])


## 3. Challenge: Do Older Players Play Less? ##

print(wnba['MIN'].mean())
print(wnba['Age'].mean())
# Let's hypothesize that older players generally play less than this average of 497 minutes, while younger players generally play more. 
wnba['age_mean_relative']=wnba['Age'].apply(lambda x: 'young' if x<27 else 'old')
wnba['min_mean_relative']=wnba['MIN'].apply(lambda x: 'average or above' if x>=497 else 'below average')
print(wnba[['Name', 'Age', 'age_mean_relative', 'MIN', 'min_mean_relative']].head())
sns.countplot(x='age_mean_relative', hue='min_mean_relative', data=wnba)
result='rejection'
print('The result of our hypothesis that older players generally play less than the average of 497 minutes, while younger players generally play more:', result)

## 4. Comparing Histograms ##

import matplotlib.pyplot as plt
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)
plt.axvline(497, label = 'Average')
plt.legend()

## 5. Kernel Density Estimate Plots ##

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)
plt.axvline(497, label='Average')
plt.legend()

'''We can still observe that most of the old players that belong to the "average or above" category play significantly more than average. With the help of the vertical line, the pattern is very easy to notice. Because the graph looks much cleaner than the one with step-type histograms, we can easily argue that the pattern is much more obvious in the case of kernel density plots.'''

## 7. Strip Plots ##

#sns.stripplot(x = 'Pos', y = 'Height', data = wnba, jitter = True)
sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
'''The patterns we see are strikingly similar to those we saw for heights. This can be easily explained by the fact that there's a strong positive relation between a player's height, her weight and her position in the game: the taller the player hence with good weight are mostly in centers; while the shorter the player hence with less weight are mostly guards.'''

## 8. Box plots ##

#sns.boxplot(x = 'Pos', y = 'Height', data = wnba)
sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)

## 9. Outliers ##

# sns.boxplot(wnba[wnba['Pos'] == 'C']['Height'], whis = 4, orient = #'vertical', width = .15)

print(wnba['Games Played'].describe())
iqr = 29 - 22
lower_bound = 22 - (1.5*iqr)
upper_bound = 29 + (1.5*iqr)
print(iqr)
print(lower_bound)
print(upper_bound)
outliers_low=sum(wnba['Games Played'] < lower_bound)
outliers_high=sum(wnba['Games Played'] > upper_bound)
print(outliers_low)
print(outliers_high)
sns.boxplot(wnba['Games Played'], orient = 'vertical')