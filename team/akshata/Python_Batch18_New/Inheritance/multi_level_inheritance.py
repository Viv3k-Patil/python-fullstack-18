class A:
    def method():
        print("A")

class B:
    def method():
        print("B")


class C(A,B):
   def method():
       print("C")


obj = C()
obj.method()