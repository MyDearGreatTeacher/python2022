import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])				# x是包含1, 2, 3, 4, 5的陣列
y = x * 2									# y是x乘以2的陣列
plt.plot(x, y, "ro")							# 使用紅色圓形繪製x與y
plt.axis([-10, 10, -50, 50])				    # 設定座標軸的範圍
plt.grid()									# 顯示X軸與Y軸的格線
plt.show()
