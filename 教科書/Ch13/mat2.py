import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.square(x)
plt.plot(x, y, "ro")
plt.show()
