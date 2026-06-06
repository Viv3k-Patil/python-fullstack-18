

def method1(a,b):
    print("method1")
    a/b

def method2():
    print("method2")
    method1(1,0)

def method3():
    print("method3")
    method2()

method3()
print("works!!")


