def add(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

print(add(1))
print(add(1, 2)) 
print(add(1, 2, 3)) 
print(add(1, 2, 3, 4))
print(add(1, 2, 3, 4, 5))
