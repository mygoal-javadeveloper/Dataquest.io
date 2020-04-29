## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,6,110)
y = -2 * x + 3
plt.plot(x,y)
plt.show()

## 6. Power Rule ##

slope_one = 5 * (2 ** 4)
print(slope_one)

slope_two = 9 * (0 ** 8)
print(slope_two)

## 7. Linearity Of Differentiation ##

slope_three = 5 * (1 ** 4) - 1
print(slope_three)

slope_four = 3 * (2 ** 2) - 2 * (2 ** 1)
print(slope_four)

## 8. Practicing Finding Extreme Values ##

rel_min = []
rel_max = []
derivative = 3 * (x ** 2) - 2 * (x) 
critical_points = [0, 2/3]
rel_min = [2/3]
rel_max = [0]