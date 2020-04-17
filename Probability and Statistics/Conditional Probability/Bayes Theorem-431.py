## 1. Independence vs. Exclusivity ##

statement_1 = False
print(statement_1)

statement_2 = True
print(statement_2)

statement_3 = True
print(statement_3)

## 2. Example Walk-through ##

p_spam = 0.2388
p_secret_given_spam = 0.4802
p_secret_given_non_spam = 0.1284

p_non_spam = 1 - p_spam
print(p_non_spam)

p_spam_and_secret = p_spam * p_secret_given_spam
print(p_spam_and_secret)

p_non_spam_and_secret = p_non_spam * p_secret_given_non_spam
print(p_non_spam_and_secret)

p_secret = p_spam_and_secret + p_non_spam_and_secret
print(p_secret)

## 3. A General Formula ##

p_boeing = 0.73
p_airbus = 0.27
p_delay_given_boeing = 0.03
p_delay_given_airbus = 0.08

p_delay = p_boeing * p_delay_given_boeing + p_airbus * p_delay_given_airbus
print(p_delay)

## 4. Formula for Three Events ##

p_boeing = 0.62
p_airbus = 0.35
p_erj = 0.03
p_delay_boeing = 0.06 
p_delay_airbus = 0.09
p_delay_erj = 0.01

p_delay =p_boeing * p_delay_boeing + p_airbus * p_delay_airbus + p_erj * p_delay_erj
print(p_delay)


## 6. Bayes' Theorem ##

p_boeing = 0.73
p_airbus = 0.27
p_delay_given_boeing = 0.03
p_delay_given_airbus = 0.08
p_delay = (p_boeing * p_delay_given_boeing) + (p_airbus * p_delay_given_airbus)
print(p_delay)
p_airbus_delay = (p_airbus * p_delay_given_airbus) / p_delay
print(p_airbus_delay)

## 7. Prior and Posterior Probability ##

p_spam = 0.2388
p_secret_given_spam = 0.4802
p_secret_given_non_spam = 0.1284

p_non_spam = 1 - p_spam
p_secret = (p_spam * p_secret_given_spam) + (p_non_spam * p_secret_given_non_spam)
print(p_non_spam)
print(p_secret)
p_spam_given_secret = (p_spam * p_secret_given_spam) / p_secret
print(p_spam_given_secret)

prior = p_spam
posterior = p_spam_given_secret

ratio = posterior / prior

print(ratio)