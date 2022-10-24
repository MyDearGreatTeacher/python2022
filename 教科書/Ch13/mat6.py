import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2
plt.plot(x, y, "ro")
# 在圖表上方顯示標題且位置為靠右
plt.title("Y = X * 2", loc = "right")
plt.show()
