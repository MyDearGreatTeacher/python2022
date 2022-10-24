import math

def e(n):  
    return sum([1 / math.factorial(i) for i in range(n)]) 

print(e(5))
print(e(10))
print(e(100))
print(e(1000))


