

<<<<<<< HEAD
print("Inside main method program is running..!!")
=======
print("Inside main method, program is running..!!")
>>>>>>> 8ee2b4665817a3550d1895555cb83836724637f7
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