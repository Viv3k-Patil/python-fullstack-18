class A:
    def __init__(self):
        super().__init__()
        self.a_attribute = "a"

    def method(self):
        print("A")

class B:
    def __init__(self):
        super().__init__()
        self.b_attribute = "b"

    def method(self):
        print("B")

class C(A, B):
    def __init__(self):
        super().__init__()
        self.c_attribute = "c"  
    

a = C()
print(C.__mro__)

# __mro__
# mro()

