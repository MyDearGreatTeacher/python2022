class A:
    x = 1

class B(A):
    y = 2

class C(B):
    z = 3
    
obj = C()
print("x屬性的值為", obj.x)
print("y屬性的值為", obj.y)
print("z屬性的值為", obj.z)