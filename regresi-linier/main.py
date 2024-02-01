import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("output_fm.csv")

d_obs = df["y_noise"]
xi = np.array(df["xi"])
d_obs[0] += 0.5

# inversi
a = 1
b = 0.5
m = [a, b]

d = np.zeros(len(xi))
def f(m):
    for i in range(len(xi)):
        d[i] = m[0] + m[1]*xi[i] # T = a + bz
    return d

d = f(m)

G = np.column_stack([xi**0, xi])

m_calc = (np.linalg.inv(np.transpose(G).dot(G)).dot(np.transpose(G))).dot(d)
d_calc = f(m_calc)
print(m_calc)

We = np.identity(np.len(xi))

# plot
plt.plot(xi, d_calc, label="data kalkulasi")
plt.plot(xi, d_obs, 'ro', label="data observasi")
plt.legend()
plt.show()