## 1. Complex Probability Problems ##

p_a = 12 / 100
print(p_a)
p_b = 17 / 100
print(p_b)
p_a_and_b = 3 / 100
print(p_a_and_b)
p_a_or_b = (12+17-3) / 100
print(p_a_or_b)

## 2. Opposite Events ##

p_non_basic = 1 - 0.20
print(p_non_basic)
p_non_premium = 1 - 0.15
print(p_non_premium)
p_subscription = 0.15 + 0.20 
print(p_subscription)
p_non_subscription =  1 - p_subscription
print(p_non_subscription)

## 3. Example Walk-Through ##

p_non_b =  7/8
print(p_non_b)
p_b = 1 - p_non_b
print(p_b)


## 4. Set Complements ##

p_non_click = 1 - 0.5
print(p_non_click)
p_two_or_less = 3/4
print(p_two_or_less)
p_three_or_more = 1 - 3/4
print(p_three_or_more)

## 5. The Multiplication Rule ##

p_6_6 = 1/6 * 1/6
print(p_6_6)
p_3_2 = 1/6 *1/6
print(p_3_2)
p_even_even = 3/6 *3/6
print(p_even_even)
p_1_even = 1/6 * 3/6
print(p_1_even)

## 6. Independent Events ##

p_18h = (1/2) ** 18
print(p_18h)
p_666 = (1/6) ** 3
print(p_666)
p_not_6 = (5/6) ** 4
print(p_not_6)

## 7. Combining Formulas ##

p_one_double_6 = 1-((35/36)**24)
print(p_one_double_6)

## 8. Sampling With(out) Replacement ##

p_kk = 4/52* 3/51
print(p_kk)
p_7q = 1/52 * 1/51
print(p_7q)
p_jqkj = 4/52 * 1/51 * 4/50 * 3/49
print(p_jqkj)