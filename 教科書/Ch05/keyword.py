def trapezoidArea(top, bottom, height):
    area = (top + bottom) * height / 2    
    print("這個梯形面積為", area)

trapezoidArea(10, 20, 5)
trapezoidArea(10, height = 5, bottom = 20)
trapezoidArea(height = 5, bottom = 20, top = 10)
