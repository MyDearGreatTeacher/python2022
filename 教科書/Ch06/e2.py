import math

def e(n):
    result = 0
    for i in range(n):
        result += 1 / math.factorial(i)
    return result

print(e(5))
print(e(10))
print(e(100))
print(e(1000))

