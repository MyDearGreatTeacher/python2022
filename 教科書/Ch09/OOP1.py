class Circle:
    PI = 3.14
    radius = 1

    def getArea(self):
        return self.PI * self.radius * self.radius

C1 = Circle()
print("半徑為", C1.radius, "的圓面積為", C1.getArea())

C2 = C1
C2.radius = 10
print("半徑為", C1.radius, "的圓面積為", C1.getArea())
