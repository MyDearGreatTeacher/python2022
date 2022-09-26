def arithmeticMean(*numbers):
    sum = 0
    n = 0
    for i in numbers:
        sum += i
        n += 1
    return sum / n


def geometricMean(*numbers):
    product = 1
    n = 0
    for i in numbers:
        product *= i
        n += 1  
    return product ** (1 / n)

print("這組資料的算術平均數為", arithmeticMean(1, 4, 5, 6, 7, 3, 8, 4, 9))
print("這組資料的幾何平均數為", geometricMean(1, 4, 5, 6, 7, 3, 8, 4, 9))
