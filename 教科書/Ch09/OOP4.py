class Circle:
    PI = 3.14
    
    def __init__(self, r = 1):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return self.PI * self.__radius * self.__radius

C1 = Circle(10)
print("C1的半徑為", C1.__radius)
print("C1的圓面積為", C1.getArea())