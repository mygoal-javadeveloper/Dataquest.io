## 1. Why Learn Calculus? ##

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 100)
y = -1*(x**2) + x*3 - 1
print(x)
print(y)

plt.plot(x,y)
plt.show()


## 4. Math Behind Slope ##

def slope(x1,x2,y1,y2):
    ## Finish the function here
    return (y2 - y1)/(x2 - x1)
slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)
print(slope_one)
print(slope_two)

## 6. Secant Lines ##

import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    # Add your code here.
    x1 = x_values[0]
    x2 = x_values[1]
    y1 = -1*(x1**2) + x1*3 - 1
    y2 = -1*(x2**2) + x2*3 - 1
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    y_secant = (m * x) + b
    plt.plot(x, y_secant, c = 'green')
    plt.show()
    
    
    
draw_secant([3,5])
draw_secant([3,10])
draw_secant([3,15])
    