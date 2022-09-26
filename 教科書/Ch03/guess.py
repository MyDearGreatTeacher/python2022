# 匯入random模組
import random
# 隨機產生一個範圍介於1 ~ 3的整數並指派給變數num
num = random.randint(1, 3)
# 取得使用者輸入的數字並指派給變數answer
answer = eval(input("請猜數字1 ~ 3："))
# 印出兩者比較的結果，True表示猜中了，False表示猜錯了
print(num, "==", answer, "is", num == answer)

