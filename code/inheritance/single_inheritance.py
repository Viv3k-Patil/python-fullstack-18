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