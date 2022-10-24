import numpy as np
import matplotlib.pyplot as plt

# 從三角形分佈取樣
samples = np.random.triangular(-3, 0, 8, 10000)
# 繪製直方圖 (分成100組)
plt.hist(samples, bins = 100)
# 顯示直方圖
plt.show()
