num = eval(input("請輸入1 ~ 10的正整數："))
# 將變數result的初始值設定為1，用來存放階乘
result = 1
# 將變數i的初始值設定為1，用來做為計數器
i = 1

# 當i小於等於num時，就將i累乘到result，再將i遞增1
while i <= num:
    result = result * i
    i = i + 1

print("{0}階乘為{1}".format(num, result))
