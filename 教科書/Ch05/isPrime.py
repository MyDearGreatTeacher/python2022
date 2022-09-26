def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True        

for i in range(2, 100):
    if isPrime(i):
        print(i)
    
