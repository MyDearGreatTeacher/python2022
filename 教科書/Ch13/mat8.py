import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2
# 透過選擇性參數label指定圖例的文字
plt.plot(x, y, "ro", label = "Y = X * 2")
# 在圖表內顯示圖例
plt.legend()
plt.show()

