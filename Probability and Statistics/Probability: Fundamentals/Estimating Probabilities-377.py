## 2. The Empirical Probability ##

p_tail = 44 / 100
print(p_tail)
p_six = 28 / 200
print(p_six)
p_odd = 102 / 200
print(p_odd)

## 3. Probability as Relative Frequency ##

p_heads_1 = (300 - 162) / 300
print(p_heads_1)
percentage_1 = p_heads_1 * 100
print(percentage_1)
p_heads_2 = (5000 - 2450) / 5000
print(p_heads_2)
percentage_2 = p_heads_2 * 100
print(percentage_2)


## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    # Uncomment above and complete code from here
    outcome = coin_toss()
    if outcome == 'HEAD':
        heads += 1
    current_probability = heads / n
    probabilities.append(current_probability)
        
print(probabilities[:10])
print(probabilities[-10:])



## 5. The True Probability Value ##

from numpy.random import seed, randint

p_l = 87 / 200 
p_l_and_c = 40 / 200
p_h = 63 / 200
p_no = (200-160) / 200
print(p_l)
print(p_l_and_c)
print(p_h)
print(p_no)

## 6. The Theoretical Probability ##

p_5 = 1 / 6
print(p_5)
p_ht = 1 / 4
print(p_ht)
p_tt = 1 / 4
print(p_tt)


## 7. Events vs. Outcomes ##

p_even = 3 / 6
print(p_even)
p_odd_no_3 = 2 / 6
print(p_odd_no_3)
p_odd_greater_5 = 0 / 6
print(p_odd_greater_5)

## 8. A Biased Die ##

p_blue = 10 / 100
print(p_blue)
p_red = 90 / 100
print(p_red)
