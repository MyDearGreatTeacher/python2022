import numpy as np
import matplotlib.pyplot as plt

HW = np.loadtxt("HW.txt", delimiter = ",")
Heights = HW[:, 0]
Weights = HW[:, 1]
plt.scatter(Heights, Weights)
plt.xlabel("Heights (cm)")
plt.ylabel("Weights (kg)")
plt.show()
