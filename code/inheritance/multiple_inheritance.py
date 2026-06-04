class A:
    def __init__(self):
        super().__init__()


    def method(self):
        print("A")

class B:
    def __init__(self):
        super().__init__()

    def method(self):
        print("B")


class C(A,B):
    def __init__(self):
        super().__init__()
        self.attribute_c="c"

    def method(self):
        print("C")

a=C()
#a.method()
#print(C.__mro__) 
print("something")
        
class C(A, B):
    def __init__(self):
        super().__init__()
        self.c_attribute = "c"  
    

a = C()
print(C.__mro__)

# __mro__
# mro()


