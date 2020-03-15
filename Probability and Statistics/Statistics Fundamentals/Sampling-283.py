## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
print(wnba.head())
print(wnba.tail())
print(wnba.shape)
#boolval = (wnba['Games Played'] >= 2016 and wnba['Games Played'] <= 2017)
parameter = max(wnba['Games Played'])
print(parameter)
sample = wnba['Games Played'].sample(30, random_state = 1)
print(sample)
statistic = max(sample)
print(statistic)
sampling_error = parameter - statistic
print(sampling_error)


## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')
print(wnba.head())
sample_means = []
population_mean = wnba['PTS'].mean()
for i in range(100):
    sample_means.append((wnba['PTS'].sample(10, random_state = i)).mean())
plt.scatter(range(1, 101), sample_means)
plt.axhline(population_mean)

## 7. Stratified Sampling ##

print(wnba['Pos'].unique())
wnba['points_per_game'] = wnba['PTS'] / wnba['Games Played']
print(wnba.head())
fstratify = wnba[wnba.Pos == 'F']
gfstratify = wnba[wnba.Pos == 'G/F']
gstratify = wnba[wnba.Pos == 'G']
cstratify = wnba[wnba.Pos == 'C']
fcstratify = wnba[wnba.Pos == 'F/C']
samplefstratify = fstratify['points_per_game'].sample(10, random_state = 0)
samplegfstratify = gfstratify['points_per_game'].sample(10, random_state = 0)
samplegstratify = gstratify['points_per_game'].sample(10, random_state = 0)
samplecstratify = cstratify['points_per_game'].sample(10, random_state = 0)
samplefcstratify = fcstratify['points_per_game'].sample(10, random_state = 0)
sampledict = {}
sampledict['F'] = samplefstratify.mean()
sampledict['GF'] = samplegfstratify.mean()
sampledict['G'] = samplegstratify.mean()
sampledict['C'] = samplecstratify.mean()
sampledict['F'] = samplefcstratify.mean()
print(sampledict)
position_most_points = max(sampledict, key=sampledict.get)
print(position_most_points)

## 8. Proportional Stratified Sampling ##

under_12 = wnba[wnba['Games Played']<=12]
btw_13_22=wnba[(wnba['Games Played']>=13) & (wnba['Games Played']<=22)]
over_23=wnba[wnba['Games Played']>=23]
proportional_sampling_means = []
for i in range(100):
    sample_under_12 = under_12['PTS'].sample(1, random_state=i)
    sample_btw_13_22 = btw_13_22['PTS'].sample(2, random_state=i)
    sample_over_23 = over_23['PTS'].sample(7, random_state=i)
    final_sample = pd.concat([sample_under_12,sample_btw_13_22,sample_over_23])
    proportional_sampling_means.append(final_sample.mean())
   
plt.scatter(range(1,101), proportional_sampling_means)
plt.axhline(wnba['PTS'].mean())

## 10. Cluster Sampling ##

samples = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)
print(samples)
df = pd.DataFrame()
for x in samples:
    df = df.append(wnba[wnba['Team']==x])
print(df.head())
sampleheight = df['Height'].mean()
sampleage = df['Age'].mean()
samplebmi = df['BMI'].mean()
sampletotalpoints = df['PTS'].mean()
print()
print(sampleheight)
print(sampleage)
print(samplebmi)
print(sampletotalpoints)
sampling_error_height = wnba['Height'].mean() - sampleheight
sampling_error_age = wnba['Age'].mean() - sampleage
sampling_error_BMI= wnba['BMI'].mean() - samplebmi
sampling_error_points = wnba['PTS'].mean() - sampletotalpoints
print()
print(sampling_error_height)
print(sampling_error_age)
print(sampling_error_BMI)
print(sampling_error_points)