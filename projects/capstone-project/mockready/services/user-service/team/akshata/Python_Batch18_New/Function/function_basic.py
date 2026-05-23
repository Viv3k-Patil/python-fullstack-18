
# function without parameter

def fuction_name():
    print("inside a function...!")

fuction_name()


# function with parameter

def greet(name):
    print(f"Hello {name}")

greet("Aksha")

#function with return value

def greet():
    return "Newgen"


def PI():
    return 3.145321

print(PI())



# check user age is valid or not

def is_user_eligible_for_driving(user_age):
    if user_age > 18:
        print("user is eligible for driving...!")
    else:
        print("Try again few years...!")

is_user_eligible_for_driving(18)




def new_function(user_name="User"):
    print("Inside a new function..!")
    print(user_name)
    print("Inside function ends ...!")

new_function()
new_function("Akshata")


def add(a,b):
    print(a+b)

add(a=10 , b= 20)


def add(*num):
    print(sum(num))

add(10,20,30,40)



def new_function():
    print("Inside new_function")

def decorator(input_func):
    print(input_func())
    print("inside decorator..!")

decorator(new_function)



def outer_function():

    def inner_function():
        print("Inside inner function")
    inner_function()
    print("inside outer function")

outer_function()



# def log_decorator(func):
#     def new_function():
#      print("------Calling inside function...!")
#      func()
#      print("------Ends with function...!")
#     return new_function


# @log_decorator
# def greet():
#     print("Hello ,Welcome to greet family..!")

# greet()


# decorator with multiple argument
def log_decorator(func):
    def new_function(*args):
     print("------Calling inside function...!")
     func(*args)
     print("------Ends with function...!")
    return new_function

def greet():
    print("Save log's!")

@log_decorator
def greet2(name):
    print(f"Hello {name}, Welcome to greet family..!")


greet()
greet2("AKshata")
