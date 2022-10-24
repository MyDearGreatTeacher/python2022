import numpy as np
import matplotlib.pyplot as plt

plt.xlabel("Age")
plt.ylabel("Monthly Salary")
plt.xticks(np.arange(7), ("", "<=20", "21~30", "31~40", "41~50", ">=51", ""))
plt.yticks(np.arange(6), ("", "<25K", "25K~35K", "35K~45K", ">45K", ""))
plt.minorticks_on()
plt.show()
