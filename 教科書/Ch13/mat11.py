import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
plt.subplot(221)
plt.plot(x, np.power(x, 1))
plt.subplot(222)
plt.plot(x, np.power(x, 2))
plt.subplot(223)
plt.plot(x, np.power(x, 3))
plt.subplot(224)
plt.plot(x, np.power(x, 4))
plt.show()