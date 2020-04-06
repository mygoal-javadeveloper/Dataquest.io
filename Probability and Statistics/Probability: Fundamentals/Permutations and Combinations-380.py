## 1. The Rule of Product ##

n_outcomes = 6 * 6
print(n_outcomes)
p_six_six = 1/36
print(p_six_six)
p_not_five_five = 1 - (1/36)
print(p_not_five_five)


## 2. Extended Rule of Product ##

total_outcomes = (6 ** 3) * 52
print(total_outcomes)
p_666_ace_diamonds = 1/total_outcomes
print(p_666_ace_diamonds)
p_no_666_ace_diamonds  = 1 - p_666_ace_diamonds
print(p_no_666_ace_diamonds)


## 3. Example Walkthrough ##

p_crack_4 = 1/10000
print(p_crack_4)
p_crack_6 = 1/1000000
print(p_crack_6)

## 4. Permutations ##

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
permutations_1 = factorial(6)
print(permutations_1)
permutations_2 = factorial(52)
print(permutations_2)
    

## 5. More About Permutations ##

def calpermutations(totalnum, knum):
    permutenum = totalnum
    for i in range(1, knum):
        permutenum *= totalnum - i
    return permutenum


perm_3_52 = calpermutations(totalnum = 52, knum = 3)
print(perm_3_52)
perm_4_20 = calpermutations(totalnum = 20, knum = 4)
print(perm_4_20)
perm_4_27 = calpermutations(totalnum = 27, knum = 4)
print(perm_4_27)
    

## 6. Permutations Formulas ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n , k):
    return factorial(n) / factorial(n-k)

p_crack_pass = 1/permutation(127, 16)
print(p_crack_pass)

## 7. Unique Arrangements ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def permutation(n, k):
    numerator = factorial(n)
    denominator = factorial(n-k)
    return numerator/denominator

c = permutation(52,5) / factorial(5)
print(c)
p_aces_7 = 1/c
print(p_aces_7)
c_lottery = permutation(49, 6) / factorial(6)
print(c_lottery)
p_big_prize = 1 /c_lottery
print(p_big_prize)




## 8. Combinations ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

c_18 = combinations(34, 18)
print(c_18)
p_non_Y = 1 - (1/c_18)
print(p_non_Y)
    