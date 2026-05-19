

<<<<<<< HEAD
print("Inside main method program is running..!!")
=======
print("Inside main method, program is running..!!")
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
def method1():
    print("Inside method 1")
    raise ValueError("An error occured")

def method2():
    print("Inside method 2")
    try:
      method1()
    except ValueError:
        raise Exception("this is different exception")

def method3():
    print("Inside method 3")
    try:
     method2()
    except Exception:
       print("Handle..!")

       
method3()