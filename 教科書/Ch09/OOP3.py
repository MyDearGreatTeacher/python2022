class Circle:
    PI = 3.14
    
    def __init__(self, r = 1):
        self.radius = r    

    def getArea(self):
        return self.PI * self.radius * self.radius

print("半徑為", Circle().radius, "的圓面積為", Circle().getArea())
print("半徑為", Circle(10).radius, "的圓面積為", Circle(10).getArea())
