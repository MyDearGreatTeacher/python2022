class ShoppingCar():
    def __init__(self, owner):
        self.__owner = owner
        self.__product = []
        
    def getOwner(self):
        return self.__owner

    def addProduct(self, product):
        self.__product.append(product)

    def removeProduct(self, product):
        self.__product.remove(product)
    
    def getProduct(self):
        return self.__product
    
obj = ShoppingCar("小丸子")
obj.addProduct("巧克力")
obj.addProduct("咖啡豆")
obj.addProduct("馬卡龍")
obj.addProduct("草莓果醬")
obj.addProduct("手工餅乾")
obj.removeProduct("咖啡豆")
print(obj.getOwner(), "的購物車裡面有", obj.getProduct())