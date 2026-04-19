# def log_decorator(func):
#     def new_function(*args):
#         print(f"_________Calling function {func}")
#         func(*args)
#         print(f"_________End function {func}")
#     return new_function


# @log_decorator
# def greet():
#     print("saving user in database")

# @log_decorator
# def gree2(name):
#     print(f"Hello {name}, this is greet2 function")


# greet()
# gree2("John") 

# def log_decoretor(func):
#     def sum(*args):
#         print("inside sum function")
#         result=func(*args)
#         print("inside sum")
#         return result
#     return sum


# @log_decoretor
# def add(a,b):
#     return a + b
# print(add(4,4))

# # Assigning a function to a variable
# def grret(n):
#     return f"hello,{n}..!"
# say_hello=grret
# print(say_hello("alex"))

# # Passing a function as an argument
# def apply(x,y):
#     return x(y)
# res= apply(say_hello,"ellon")
# print(res)


# #multi
# def multi(x):
#    def double_multi(y):
#         print("addition")
#         return x*y
#    return double_multi
   
# db1=multi(2)
# print(db1(5))


# def fun(x,y):
#     return x(y)

# def square(x):
#     return x*x
# res=fun(square,5)
# print(res)


# def my_decoretors(func):
#     def wrapper(self,*args,**kwagrs):
#         print("Before method execution")
#         res = func(self,*args,**kwagrs)
#         print("After method execution")
#         return res
#     return wrapper
        


# class MyClass:
#     @my_decoretors
#     def my_func(self):
#         print("say hello")
# a=MyClass()
# a.my_func() 

# user = ["John", "Alice", "Bob"]

# def auth(func):
#     def auth_wrapper(*args):
#         if args[0] in user:
#             func(*args)
#         else:
#             print("Unauthorized access!! Log in with valid user")
#     return auth_wrapper

# @auth
# def access_private_data(name):
#     print("Accessing private data and secrets")

# @auth
# def access_private_data2(name):
#     print("Accessing private data and secrets 2")

# access_private_data("Bob")
# access_private_data2("Johny")
         
users=["sham","ram"]

def log_decoretor(func):
    def wrpper(*args):
        if args[0] in users:
            func(*args)
        else:
            print("unothrized user")
    return wrpper
@log_decoretor
def accesprivate_data_and_access(name):  
    print("accessing data")     

def accesprivate_data_and_access1(name):  
    print("accessing data 1")    

accesprivate_data_and_access("sham")    



