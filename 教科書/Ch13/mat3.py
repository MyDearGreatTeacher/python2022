import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
plt.plot(x, x, "r--", x, x ** 2 , "bs", x, x ** 3, "g^")
plt.show()
