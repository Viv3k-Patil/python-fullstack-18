
# # # function with argument
# # def say_hello(age: int):
# #     print(f"hello there!!{age}")

# # say_hello(18)

# # # decorator is a function that takes function as an argumnet

# # def my_decorator(func):
# #     # function body

# def auth_required(func):
#     def wrapper(*args, **kwargs):
#         user = kwargs.get("user")

#         if not user:
#             return {"error": "Unauthorized"}

#         return func(*args, **kwargs)

#     return wrapper

# @auth_required
# def get_data(user=None):
#     return {"data": "secret data"}

# get_data()
    
# def my_decorator(func):
#     def wrapper(*args):
#         result = func(*args)
#         print("something wrapper function")
#         print(result)
#     return wrapper

# def my_anotherdecorator(func):
#     def wrapper(*args):
#             print("inside another function")
#     return wrapper

# @my_anotherdecorator
# @my_decorator
# def say_hello(a,b):
#     return a+b

# say_hello(5,3)


# def my_function():
#     print("this is my function")

# a = my_function

# a()

# # function 2
# def new_functioin2():
#     print("inside function 2")

# # function 1
# def new_function():
#     print("inside new function")

# # decorator function
# def decorator(input_func):
#     print(input_func)
#     print("inside decorator")

# decorator(new_function)

# def outer_function():
#     # outer function codeblock
#     def inner_function():
#         print("inside inner function")
    
#     inner_function()
#     print("inside outer function")

# outer_function()


def log_decorator(func):
    def new_function():
        print(f"_________Calling function {func}")
        func()
        print(f"_________End function {func}")
    return new_function



def greet():
    print("saving user in database")

@log_decorator
def gree2():
    print("Hello greet2 function")


greet()
gree2()
