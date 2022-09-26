def F(n):
    if n == 0:                  # 當N = 0時，F(N) = N! = 0! = 1 
        return 1
    elif n > 0:
        return n * F(n - 1)     # 當N > 0時，F(N) = N! = N * F(N - 1)
    else:
        return -1               # 當N < 0時，F(N) = -1，表示無法計算階乘 

print("0! =", F(0)) 
print("5! =", F(5))

