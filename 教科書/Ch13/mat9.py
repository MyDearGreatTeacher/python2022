import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2
plt.figure(figsize = (6, 4), facecolor = "lightblue")
plt.plot(x, y, "ro")
plt.show()
