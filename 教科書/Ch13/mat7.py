import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2
plt.plot(x, y, "ro")
# 在座標為 (1, 10) 處顯示文字
plt.text(1, 10, "Y = X * 2")
plt.show()

