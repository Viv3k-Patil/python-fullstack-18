

class A():
    def __init__(self):
        self.a_attribute="a_attribute"
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        self.a_attribute="b_attribute"
        print("B")

B()   
print("something") 

class A:
    def __init__(self):
        self.a_attribute = "a_attribute"
        super().__init__()
        print("A")

    def print_b():
        print("inside A class")

class C:
    def __init__(self):
        self.c_attribute = "c_attribute"
        print("C")

    def print_c():
        print("inside C class")

class B(A,C):
    def __init__(self):
        self.b_attribute = "b_attribute"
        super().__init__()
        print("B")



a = B()

print(B.__mro__)

