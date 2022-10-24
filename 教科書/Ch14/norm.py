import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

loc, scale = 0, 1
x = np.linspace(stats.norm.ppf(0.01, loc, scale), stats.norm.ppf(0.99, loc, scale), 100)
plt.plot(x, stats.norm.pdf(x), "r-", label = "norm pdf")

# 產生1000個標準常態分佈亂數
r = stats.norm.rvs(size = 1000)
# 將1000個亂數繪製成直方圖 (透明度為0.2)
plt.hist(r, density = True, histtype = "stepfilled", alpha = 0.2)
# 顯示圖例
plt.legend()
plt.show()