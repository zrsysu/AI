%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
​
def calcAB(x,y):
    n = len(x)
    sum_x, sum_y, sum_xy, sum_xx = 0,0,0,0
    for i in range(0, n):
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i] * y[i]
        sum_xx += x[i] * x[i]
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_xx * sum_y - sum_x * sum_xy)/(n * sum_xx - sum_x * sum_x)
    return a, b
xi = [1,2,3,4,5,6,7,8,9,10]
yi = [10,11.5,12,13,14.5,15.5,16.8,17.3,18,18.7]
a, b = calcAB(xi, yi)
print("y = %10.5fx + %10.5f" %(a,b))
x = np.linspace(0,10)
y = a * x + b
plt.plot(x,y)
plt.scatter(xi,yi)
plt.show