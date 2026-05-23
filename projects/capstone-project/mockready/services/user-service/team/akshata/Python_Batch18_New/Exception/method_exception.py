

def method1():
    print("Method1..!")
    1/0

def method2():
    print("Method2..!")
    try:
        method1()
    except Exception:
        print("can not 0 diveded by any number.")


method2()