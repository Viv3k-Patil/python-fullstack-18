# class Mobile:
#   def __init__(self,
#   mobile_name,             
#   mobile_color,
#   mobile_RAM,
#   mobile_ROM,
#   mobile_price,
#   mobile_battery
#                 ):
#      self.mobile_name=mobile_name
#      self.mobile_color=mobile_color
#      self.mobile_RAM=mobile_RAM
#      self.mobile_ROM=mobile_ROM
#      self.mobile_price=mobile_price
#      self.mobile_battery=mobile_battery

#   def __str__(self):
#      return f"mobile name:{self.mobile_name},\nmobile color:{self.mobile_color},\nmobile RAM:{self.mobile_RAM},\nmobileROM:{self.mobile_ROM},\nmobile price:{self.mobile_price},\nmobile battery:{self.mobile_battery}"
        
#   def grret( ):
#      print("this is example of grret")


#   grret()     
# a=Mobile(
#           [
#           "redmi",
#            "oppo", 
#           " vivo",
#           "samsung",
#           "iphone"
#           ],
#    "Red",
#    "8GB",
#    "256 ROM",
#     25999,
#    "5500Mph"
#     )   



# print(a)


# #class And Object

# class Batch:
#     #class body start
#     def __init__(self,
#     batch_name,
#     batch_no,             
#     batch_timings,             
#     instructor,
#     student_list             
#                  ):
#         self.batch_name = batch_name
#         self.batch_no = batch_no
#         self.batch_timings = batch_timings
#         self.instructor = instructor
#         self. student_list  =  student_list 

#     def __str__(self):
        
#         return f"batch_name: {self.batch_name},\nbatch_no: {self.batch_no}, \nbatch_timings: {self.batch_timings} \ninstructor: {self.instructor} \nstudents: {self.student_list}"
        
#     # class body ends



# a = Batch(
#         "python-ffullstack-18",
#         18,
#         "7.30am - 9.30am",
#         "Vivek Patil",
#         [
#             "Girish",
#             "Sameer",
#             "Akshada",
#             "Rushikesh"
#         ]
#     )
    
# b = Batch(
#         "MERN-fullstack-22",
#         22,
#         "7.30pm - 9.30pm",
#         "XYZ",
#         [
#             "Girish",
#             "Sameer",
#             "Akshada",
#             "Rushikesh"
#         ]
#     )

# a.instructor = "XYZ"
# print(a.instructor)
# print(a)
# print(a.)
# print(a.batch_name)
# print(a.batch_number)

# b = Batch("Java-fullstack-batch", 31)
# print(b.batch_name)
# print(b.batch_number)
# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List


# class Item(BaseModel):
#     product_name: str
#     price: float

# class Order(BaseModel):
#     order_id: int
#     items: List[Item]  # A list of Item objects

# data = {
#     "order_id": 99,
#     "items": [
#         {"product_name": "Laptop", "price": 1200.50},
#         {"product_name": "Mouse", "price": 25.00}
#     ]
# }

# a=Order(**data)
# print(a.items[1].product_name)

    


