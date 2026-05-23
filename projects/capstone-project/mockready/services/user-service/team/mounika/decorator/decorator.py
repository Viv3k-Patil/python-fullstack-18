
# # def log_decorator(func):
# #     def new_function(*args):
# #         print(f"_________Calling function {func}")
# #         func(*args)
# #         print(f"_________End function {func}")
# #     return new_function


# # @log_decorator
# # def greet():
# #     print("saving user in database")

# # @log_decorator
# # def gree2(name):
# #     print(f"Hello {name}, this is greet2 function")


# # greet()
# # gree2("John")

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

# access_private_data2("John")
# access_private_data("mounika")

def function()