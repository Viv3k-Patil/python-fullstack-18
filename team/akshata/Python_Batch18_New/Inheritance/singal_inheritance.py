class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(Self):
        super().__init__()
        print("B")

obj = B()
