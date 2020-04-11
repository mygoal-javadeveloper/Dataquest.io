## 2. Brief Recap ##

p_2 = 1/6
print(p_2)
p_odd = 3/6
print(p_odd)
p_2_or_4 = 2/6
print(p_2_or_4)

## 3. Updating Probabilities ##

p_3 = 1/4
print(p_3)
p_6= 0/4
print(p_6)
p_odd = 2/4
print(p_odd)
p_even = 2/4
print(p_even)

## 4. Conditional Probability ##

p_december = 1/3
print(p_december)
p_31 = 2/3
print(p_31)
p_summer = 0/3
print(p_summer)
p_ends_r = 1/3
print(p_ends_r)

## 5. Conditional Probability Formula ##

card_b = 21
card_a_and_b = 9
p_a_given_b = 9/21
print(card_b)
print(card_a_and_b)
print(p_a_given_b)

## 6. Example Walkthough ##

p_negative_given_non_hiv = 6/30
print(p_negative_given_non_hiv)

'''The probability of testing negative given that a patient is not infected with HIV is 20%. This means that for every 10,000 healthy patients, only about 2000 will get a correct diagnosis, while theother 8000 will not. It looks like the test is almost completely inefficient, and it could be dangerous to have it used in hospitals.'''




## 7. Probability Formula ##

p_premium_given_chrome = 158/2762
print(p_premium_given_chrome)

p_basic_given_safari = 274/1288
print(p_basic_given_safari)

p_free_given_firefox = 2103/2285
print(p_free_given_firefox)

more_likely_premium = 'Chrome' if 158/2762 > 120/1288 else 'Safari'
print(more_likely_premium)