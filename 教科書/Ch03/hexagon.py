import math
s = eval(input("請輸入正六邊形的邊長："))
area = 6 * s * s / (4 * math.tan(math.pi / 6))
print("邊長", s, "的正六邊形面積為", area)

