import matplotlib.pyplot as plt
import numpy as np
import random as rnd

x = np.array(range(-10,10,1))
a = 1
b = 0.1
c = 0.1
d = 0.015
e = 0.00001

y = a+b*x+c*(x**2) + d*(x**3) + e*(x**4)

rng = np.random.default_rng()
yn = y + 0.5*rng.normal(size=20)
plt.plot(x,y, 'b-')
plt.plot(x,yn, 'ro')
plt.title("Orde 4")
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()
print(y)
print(yn)