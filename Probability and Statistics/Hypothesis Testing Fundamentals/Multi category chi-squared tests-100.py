## 2. Calculating expected values ##

males_over50k = .67 * .241 * 32561
print(males_over50k)
males_under50k = .67 * .759 * 32561
print(males_under50k)
females_over50k = .33 * .241 * 32561
print(females_over50k)
females_under50k = .33 * .759 * 32561
print(females_under50k)

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]
chisq_gender_income = 0
for idx, obs in enumerate(observed):
    chisq_gender_income = chisq_gender_income + ((obs - expected[idx]) ** 2) / expected[idx]
    
print(chisq_gender_income)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5257.6, 2589.6, 16558.2, 8155.6])
chisquare_value, pvalue_gender_income = chisquare(observed, expected)

print(chisquare_value)
print(pvalue_gender_income)

## 5. Cross tables ##

import pandas

table1 = pandas.crosstab(income["sex"], [income["high_income"]])
print(table1)

table = pandas.crosstab(income['sex'], [income['race']])
print(table)

## 6. Finding expected values ##

import numpy as np
from scipy.stats import chi2_contingency
observed = np.array([[5, 5], [10, 10]])

chisq_value1, pvalue1, df1, expected1 = chi2_contingency(observed)


table = pandas.crosstab(income['sex'], [income['race']])
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)

print(chisq_value1)
print(pvalue1)
print(df1)
print(expected1)
print()
print(chisq_value)
print(pvalue_gender_race)
print(df)
print(expected)