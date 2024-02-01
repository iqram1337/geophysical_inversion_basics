import matplotlib.pyplot as plt
import numpy as np
import random as rnd
x = np.array(range(-10, 10, 1))
a = 1
b = 0.1
c = 0.1
d = 0.015
e = 0.00001

# Koefisien polinomial
m = np.array([a, b, c, d, e])

# Matriks polinomial dengan orde 4
G = np.column_stack([x**0, x, x**2, x**3, x**4])
# G = [np.ones(20), x, x**2, x**3, x**4]
# Gt = np.transpose(G)
# y = np.matmul(Gt,m)

# Hitung nilai y menggunakan perkalian matriks
y = G.dot(m)

rng = np.random.default_rng()
noise = 0.5
yn = y + noise * rng.normal(size=20) # ada noise
yy = a + b*x + c*(x**2) + d*(x**3) + e*(x**4)

plt.plot(x,yy, 'go')
plt.plot(x, y, 'b-')
#plt.plot(x, yn, 'ro')

plt.title("Orde 4")
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-10, 10)
plt.ylim(-10, 10)
#plt.legend(['d obs', 'line d obs', f'd calc noise:{noise}'])
plt.show()
print(y)
print(yn)
