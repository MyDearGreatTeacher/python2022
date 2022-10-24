import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 建立一個範圍介於 [1, 11) 整數均勻分佈的機率模型
rv = stats.randint(low = 1, high = 11)
# 變數x是用來繪製機率質量函數的資料 (從1% ~ 99% (不含) 之間的值)
x = np.arange(rv.ppf(0.01), rv.ppf(0.99))
# 以藍色圓點繪製均勻分佈的機率質量函數
plt.plot(x, rv.pmf(x), "bo", label = "randint pmf")
# 以透明度0.5的藍色虛線繪製垂直線
plt.vlines(x, 0, rv.pmf(x), "b", linestyles = "dashed", alpha = 0.5)
plt.legend()
plt.show()