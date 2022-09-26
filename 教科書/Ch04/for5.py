num = eval(input("請輸入1 ~ 10的正整數："))
result = 1
for i in range(1, num + 1):
    result = result * i
print("{0}階乘為{1}".format(num, result))
