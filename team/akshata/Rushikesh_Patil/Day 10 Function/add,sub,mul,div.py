def add():
   a=int(input("enter the firsr number: "))
   b=int(input("enter the second number: "))
   c=a+b
   print("sum of two numbers is:",c)

def sub():
   a=int(input("enter the firsr number: "))
   b=int(input("enter the second number: "))
   c=a-b
   print("substraction of two numbers is:",c)


def mul():
    a=int(input("enter the firsr number: "))
    b=int(input("enter the second number: "))
    c=a*b
    print("multiplication of two numbers is:",c)


def div():    
    a=int(input("enter the firsr number: "))
    b=int(input("enter the second number: "))
    c=a/b
    print("division of two numbers is:",c)
print("addition: ")
add()
print("substraction: ")
sub()
print("multiplication: ")
mul()
print("division: ")
div()