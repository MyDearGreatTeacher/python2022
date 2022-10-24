matrix = []
rows = eval(input("請輸入矩陣的列數："))
cols = eval(input("請輸入矩陣的行數："))

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        element = eval(input("請輸入矩陣的元素 (由上往下逐列輸入)："))
        matrix[i].append(element)

print(matrix)





