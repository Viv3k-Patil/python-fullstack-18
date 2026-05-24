class A:
    def __init__(self):
        self.a_attribute = "a_attribute"
        super().__init__()
        print("A")

    def print_a(self):
        print("inside A class")

class C(A): 
    def __init__(self):
        self.c_attribute = "c_attribute"
        super().__init__()
        print("C")

# Execution
a = C()
print(C.__mro__)