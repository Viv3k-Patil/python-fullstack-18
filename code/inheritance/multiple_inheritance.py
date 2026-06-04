class A:
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.attribute_a="a"
=======
        self.a_attribute = "a"
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125

    def method(self):
        print("A")

class B:
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.attribute_b="b"
=======
        self.b_attribute = "b"
>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125

    def method(self):
        print("B")

<<<<<<< HEAD
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
        
=======
class C(A, B):
    def __init__(self):
        super().__init__()
        self.c_attribute = "c"  
    

a = C()
print(C.__mro__)

# __mro__
# mro()

>>>>>>> 020cde27e2bd12c348bb2f3cb5096bdd5119c125
