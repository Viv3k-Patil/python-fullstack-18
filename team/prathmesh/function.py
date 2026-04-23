# def my_function():
#     print("prathm")
#     print("prathm")
#     print("prathm")
#     print("prathm")
#     print("prathm")
#     print("prathm")

# print(my_function())


# #def area_of_rec(length,height):
     
#     #print("Enter the  len",length)
#    # print("enter the height",height)
#   #  area=length*height
#  #   print(area)
 
# #area_of_rec(10,20)



# #def addition():
#   #  add_ition=10+20
#  #   print(add_ition)

# #addition()



# #area of circle
# def PI():
#     return 3.148998

# def area_of_circle(redius):
#     return redius*redius*PI()

# print(area_of_circle(10))

# Function With Parameters
# def greet(user_name):
#     print(f"Hello, {user_name}, How are you?")

# greet("Newgen")

# #function with return vlue
# def function_name():
#     return "newgen"

# def PI():
#     return 3.14159265

# print(PI())

# #   
# def upper_case(input_string):
#     return input_string.lower()

# print(upper_case("VIVEK"))


# def user_age_eligible_for_driving(user_age):
#     if user_age>=18:
#         print("eligible to drive")
#     else:
#         print("try again in future")
# user_age_eligible_for_driving(20)        

#fuctions with defult parameters
# def new_user(name="user"):
#     print("inside function")
#     print(f"welcome,{name}")
#     print("ends fucion body here")

# new_user() 
# new_user("vivek")   

#using keyward arguments

# def user_details(name,middlename,surname):
#     print(f"your name is {name}  and lastname is {surname}")
#     print(f"your is middlename {middlename} ")

# user_details(
#     name="vivek",
#     middlename="raj",
#     surname="patil"
#     )    

# def user_age(name,age):
#     print(name,age)
# user_age(name="vivek",age=18)  

# #argu using length of parameters
# def add(*numbers):
#     print(sum(numbers))
# add(12,12,12)

# def new_fuction1():
#     print("inside new function1")

# def new_function():
#     print("inside new function")

# def decorator(input_func):
#     print(input_func)
#     print("inside decorator")

# decorator(new_fuction1)


# def outer_function():

#     def inner_function():
#         print("inside inner function")
    
#     inner_function()
#     print("inside outer function")

# outer_function()



# def log_decoretor(func):
#     def new_function():
#       print(f"calling function {func}")
#     func()
#     print(f"ending function {func}")
#     return new_function



# @log_decoretor
# def greet():
#     print("inside greet function")
#     print("inside greet function")
#     print("inside greet function")
#     print("inside greet function")

# greet()    

def log_decoretors(func):
    def sum():
        print("inside sum {func}")
        func(10,20)
        print("outside sum {func}")
        return sum

@log_decoretors
def greet(a=10,b=20):
    print(a+b)


greet()