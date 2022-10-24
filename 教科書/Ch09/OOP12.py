class Transport:
    def __init__(self, owner, CC):
        self.__owner = owner
        self.__CC = CC
        
    def getOwner(self):
        return self.__owner
    
    def getCC(self):
        return self.__CC
        
    def launch(self):
        print("在此寫上發動交通工具的敘述")

    def park(self):
        print("在此寫上停止交通工具的敘述")

class Motorcycle(Transport):
    def launch(self):
        print("在此寫上發動摩托車的敘述")
        
    def park(self):
        print("在此寫上停止摩托車的敘述")

class Car(Transport):
    def launch(self):
        print("在此寫上發動汽車的敘述")
        
    def park(self):
        print("在此寫上停止汽車的敘述")        

obj1 = Motorcycle("小明", 125)
print("這個交通工具的車主、CC數：", obj1.getOwner(), obj1.getCC())
obj1.launch()
obj1.park()

obj2 = Car("大偉", 2000)
print("這個交通工具的車主、CC數：", obj2.getOwner(), obj2.getCC())
obj2.launch()
obj2.park()



    


