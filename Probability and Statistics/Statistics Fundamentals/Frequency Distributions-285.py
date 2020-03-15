## 2. Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
freq_distro_pos=wnba['Pos'].value_counts()
print(freq_distro_pos)
freq_distro_height=wnba['Height'].value_counts()
print(freq_distro_height)


## 3. Sorting Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
age_ascending =wnba['Age'].value_counts().sort_index()
print(age_ascending)
age_descending=wnba['Age'].value_counts().sort_index(ascending=False)
print(age_descending)
print('There are no players under 20')
print('There are 30 nos of players 30 or over')

## 4. Sorting Tables for Ordinal Variables ##

def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'
    
wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

# Type your answer below
pts_ordinal_desc=wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]
print(pts_ordinal_desc)

## 5. Proportions and Percentages ##

wnba = pd.read_csv('wnba.csv')
percentages = wnba['Age'].value_counts(normalize = True).sort_index() * 100
proportion_25 = percentages[25] / 100
percentage_30 = percentages[30]
percentage_over_30 = percentages.loc[30:].sum()
percentage_below_23 = percentages.loc[:23].sum()

## 6. Percentiles and Percentile Ranks ##

from scipy.stats import percentileofscore
wnba = pd.read_csv('wnba.csv')
percentile_rank_half_less=percentileofscore(a=wnba['Games Played'], score=17,kind='weak')
print(percentile_rank_half_less)
percentage_half_more = 100-percentile_rank_half_less
print(percentage_half_more)

## 7. Finding Percentiles with pandas ##

wnba = pd.read_csv('wnba.csv')
a=wnba['Age'].describe(percentiles = [.25, .5, .75, .95])
print(a)
age_upper_quartile = a[6]
age_middle_quartile = a[5]
age_95th_percentile = a[7]
print(age_upper_quartile)
print(age_middle_quartile)
print(age_95th_percentile)
question1=True
print(question1)
question2=False
print(question2)
question3=True
print(question3)

## 8. Grouped Frequency Distribution Tables ##

wnba = pd.read_csv('wnba.csv')
grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize =True).sort_index(ascending = False)*100
print(grouped_freq_table)
                                                    

## 10. Readability for Grouped Frequency Tables ##

wnba = pd.read_csv('wnba.csv')
intervals=pd.interval_range(start=0, end=600, freq=60)
gr_freq_table_10=pd.Series([0,0,0,0,0,0,0,0,0,0], index=intervals)
for value in wnba['PTS']:
    for interval in intervals:
        if value in interval:
            gr_freq_table_10.loc[interval]+=1
            break
print(gr_freq_table_10)