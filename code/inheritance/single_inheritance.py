class A:
    def __init__(self):
        self.a_attribute = "a_attribute"
        print("A")

class B(A):
    def __init__(self):
        self.a_attribute = "b_attribute"
        super().__init__()
        print("B")

a = B()
print("somethingg")