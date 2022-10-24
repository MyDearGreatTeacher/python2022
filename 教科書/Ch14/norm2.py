import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

loc1, scale1 = 0, 1
x1 = np.linspace(stats.norm.ppf(0.001, loc1, scale1), stats.norm.ppf(0.999, loc1, scale1), 1000)
plt.plot(x1, stats.norm.pdf(x1), "r-", label = "norm1 pdf")

loc2, scale2 = 2, 1
x2 = np.linspace(stats.norm.ppf(0.001, loc2, scale2), stats.norm.ppf(0.999, loc2, scale2), 1000)
plt.plot(x2, stats.norm.pdf(x2, loc2, scale2), "g--", label = "norm2 pdf")

loc3, scale3 = 0, 2
x3 = np.linspace(stats.norm.ppf(0.001, loc3, scale3), stats.norm.ppf(0.999, loc3, scale3), 1000)
plt.plot(x3, stats.norm.pdf(x3, loc3, scale3), "b:", label = "norm3 pdf")

plt.legend()
plt.show()