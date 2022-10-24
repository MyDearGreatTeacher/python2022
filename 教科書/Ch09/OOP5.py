class Employee:    
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSalary(self, basic, bonus = 0):
        self.__salary = basic + bonus

    def getSalary(self):
        return self.__salary

E1 = Employee("陳小明")
E2 = Employee("王大同")
E1.setSalary(28000)
E2.setSalary(28000, 1500)
print("員工", E1.getName(), "的薪水為", E1.getSalary())
print("員工", E2.getName(), "的薪水為", E2.getSalary())