import numpy as np
import matplotlib.pyplot as plt

# 從常態分佈取樣
samples = np.random.normal(size = 10000)
# 繪製直方圖 (分成30組)
plt.hist(samples, bins = 30)
# 顯示直方圖
plt.show()
