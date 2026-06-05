<<<<<<< HEAD


print("Inside main method program is running..!!")
=======
print("Inside main method, program is running..!!")

>>>>>>> 858f3ace40ff27d25f96d0e29f05a442a15da6e3
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