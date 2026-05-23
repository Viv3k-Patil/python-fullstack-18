class A:
    def __init__(self):
        self.a_attribute = "a_attribute"
        print("A")

class B:
    def __init__(self):
        self.b_attribute = "b_attribute"
        print("B")

class C(A, B):   
    def __init__(self):
        
        super().__init__()
        self.c_attribute = "c_attribute"
        print("C")

a = C()
print(C.__mro__)