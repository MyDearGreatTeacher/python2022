class A:
    __x = "我是屬性__x"
    y = "我是屬性y"
    
    def __M1(self):
        print("我是方法M1()")

    def M2(self):
        print("我是方法M2()")

class B(A):
    z = "我是屬性z"
    
    def M3(self):
        print("我是方法M3()")