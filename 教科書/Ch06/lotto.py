import random

# 串列變數lotto用來存放隨機產生的整數
lotto = []
# 隨機產生六個介於1 ~ 49且不重複的整數
for i in range(6):
    lotto.append(random.choice([x for x in range(1, 50) if x not in lotto]))
# 將隨機產生的六個整數由小到大排序
lotto.sort()
print(lotto)
