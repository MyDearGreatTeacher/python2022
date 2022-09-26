x1, y1 = eval(input("請輸入第一個點的座標："))
x2, y2 = eval(input("請輸入第二個點的座標："))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("兩點距離為", distance)

