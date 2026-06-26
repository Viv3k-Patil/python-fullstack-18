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




# def pizza(func):
#     def toping():
#         print("Adding toping")
#         func()
#     return toping

# @pizza
# def pizzaa():
#     print("Making pizza")

# pizzaa()

import threading
import time

def code_shikha():
    for i in range(3):
        print("coding shiktoy...")
        time.sleep(1) # १ सेकंदाचा ब्रेक

def gaणी_ऐका():
    for i in range(3):
        print("song aiktoy")
        time.sleep(1) # १ सेकंदाचा ब्रेक

# दोन वेगळे थ्रेड्स (कामगार) तयार केले
thread1 = threading.Thread(target=code_shikha)
thread2 = threading.Thread(target=gaणी_ऐका)

# दोन्ही कामे एकाच वेळी सुरू केली
thread1.start()
thread2.start()

# दोन्ही कामे संपण्याची वाट पाहणे
thread1.join()
thread2.join()

print("zal baba ekdach!")