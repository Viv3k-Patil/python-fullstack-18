
#Write a program area of rectangle with arguments

def calculate_area_of_rectangle(length , width):
     
    area_of_rectangle_formula =length * width
    print(area_of_rectangle_formula)
calculate_area_of_rectangle(10,5)


#function without parameters but returns value

def PI():
    return 3.14159265

#print(PI())

#write a program area of circle

def area_of_circle(radius):
    return radius*radius*PI()

print(area_of_circle(10))

