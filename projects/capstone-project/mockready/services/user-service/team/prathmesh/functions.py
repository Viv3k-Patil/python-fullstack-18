#def my_function():
   #print("prathm")
    #print("prathm")
    #print("prathm")
   # print("prathm")
    #print("prathm")

#print(my_function())


#def area_of_rec(length,height):
     
    #print("Enter the  len",length)
   # print("enter the height",height)
  #  area=length*height
 #   print(area)
 
#area_of_rec(10,20)



#def addition():
  #  add_ition=10+20
 #   print(add_ition)

#addition()



#area of circle
#def PI():
 #   return 3.148998

##def area_of_circle(redius):
  #  return redius*redius*PI()

#print(area_of_circle(10))

#def greet():
 #   print("Hello")

#greet()


#def addtion(a,b):
 #   return a+b
#print(addtion(10,20))


#Function Without Parameters
#def welcome():
 #   print("Welcome to python")

#welcome()
    
#Function With Parameters
#def greet(name):
 #   print("My name is",name)

#greet("rahul")    

#Function With Return Value

def root(num):
    return num*num*num

print(root(5))

#Default Parameters

#def add_item(item="apple"): 
 # return item

#print(add_item())

def add_stationary(item,list=[]):
    list.append(item)
    return list

print(add_stationary("pen"))
print(add_stationary("NoteBook"))
print(add_stationary("Pencile"))


#Keyword Arguments

#def student_info(name,surname,PRN):
 #   print("my name is",name)
  #  print("my Surname is",surname)
   # print("my PRN is",PRN)

#student_info(name="raj",surname="patil",PRN=98)    
#print(student_info)



#Variable Length Arguments (*args)
#def add_numbers(*numbers):
 #   print(numbers)

#add_numbers(1,2,3,4,5,6)    

#def total(*numbers):
  
  #result=0
  #for sum in numbers:
 #    result+= sum
#  return result

 
#print(total(10,20,30,40))

#Keyword Variable Arguments

#def Student_info(**data):
 #  print(data)

#print(type(Student_info(name="ram",age=27) )  )  #<class 'NoneType'>



#my_dictionary={
   #"name":"prathm",
  # "clg":"DYP",
 #  "age":22
#}

#print(type(my_dictionary))


#max and Min Function

#def Num_list(*numbers):
   
   #print("maximum number is:",max(numbers))
  # print("minimum number is:",min(numbers))
 #  print("index of 4 is:",numbers[4])
#Num_list(100,20,45,15,27)   


#students marks example

#marks=[10,20,50,70,55]

#print("Highest marks",max(marks))
#print("Lowest marks",min(marks))



#**maximum of two numbers**

def number(num):
   
   return num

print(number(max(20,10)))


def number(num):
   
   return num

print(number(max(5, 8, 2)))