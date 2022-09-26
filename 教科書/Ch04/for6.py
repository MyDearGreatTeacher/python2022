n = eval(input("請輸入金字塔的高度 (1 ~ 30)："))

for i in range(1, n + 1):
    print(" " * (n - i) , "*" * (2 * i - 1))
