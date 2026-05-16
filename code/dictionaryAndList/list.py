#create a list using append()

fruits=["apple","bannana"]

# fruits.append("Mango")

"""READ """
# Accessing by index
# print(fruits[0])  # Output: bannana

# # Reading all items
# for iteam in fruits:
#     print(iteam)
    
"""""UPDATE"""    
fruits[1]="Blueberry"    
print(fruits)


"""DELETE"""

#fruits.remove("apple")
  
del fruits[0]  # Delete by index
print(fruits) # Output: 'apple



""""Operation 	 Python List Method	     SQL Command    HTTP Method (API)"""
# Create	     append(), insert()	      INSERT	      POST
# Read	         index access, loops	  SELECT          GET
# Update	     list[index] = value	  UPDATE       PUT / PATCH
# Delete	     remove(), pop(),del	  DELETE         DELETE


# class students:
#     def __init__(self,id,name,batch,marks):
#         self.id=id
#         self.name=name
#         self.batch=batch
#         self.marks=marks
        
#     def change_name(self,newname):
#         self.name=newname    
        
#     def my_student_info(self):  
#         print("my name is ",self.name)  
#         print("______________________")
#         print("my id is",self.id)
#         print("______________________")
#         print("my batch is",self.batch)
#         print("______________________")
#         return print(self.name,"your marks is",self.marks*2)
        
# stud=students(1,"prathm",10,99)
# stud1=students(2,"ram",9,85)
# #stud.my_student_info()

# #stud1.my_student_info()
# #print("hello",stud.name)

# stud1.change_name("sham")
# stud1.my_student_info()



# class Car:
#     def __init__(self,brand,speed,color,shade):
#         self.brand=brand
#         self.speed=speed
#         self.color=color   
#         self.shade=shade 
        
#     def drive(self):    
#         print(self.brand,"is runnig at",self.speed , "KM/hr")
        
#     def accelarate(self,value):
#         print(self.speed + value)
  
#     def colour(self):
        
#         print(self.brand ,"color is",self.color)
#         print("and shade is ", self.shade)
        
# c=Car("BMW",100,"Blue","white-redish")        

# c.accelarate(20)
# c.drive()
# c.colour()

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def display(self):
#         print(self.name ,"your marks is",self.marks)

        
#     def update_marks(self,updated_marks):    
#         self.marks=updated_marks
        
        
# stud=Student("vivek",99)
# stud.display()        
# stud.update_marks(85)
