grades = [[95, 100, 100], [86, 90, 75], [98, 98, 96], [78, 90, 80], [70, 68, 72]]

for i in range(5):
    subTotal = 0                        # 將用來暫存每位學生總分的變數subTotal歸零
    for j in range(3):                  # 將分數累計暫存在變數subTotal
        subTotal += grades[i][j]
    grades[i].append(subTotal)          # 將累計的總分存放在二維串列


for i in range(5):
    print("學生", i + 1, "的總分為", grades[i][3])


