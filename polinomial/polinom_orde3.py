import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## polinom ordo 3
a = 1e-7
b = 1e-7
c = 1e-7
d = 1e-7

x = np.arange(-10,10)

y = a + b*x + c*(x**2) + d*(x**3)

plt.plot(x,y)

plt.show()