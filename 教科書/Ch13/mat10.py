import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y1 = 20 * np.sin(x)
y2 = x * x * np.cos(x) + 0.5
plt.subplot(211)
plt.plot(x, y1, "b-")
plt.subplot(212)
plt.plot(x, y2, "r--")
plt.show()