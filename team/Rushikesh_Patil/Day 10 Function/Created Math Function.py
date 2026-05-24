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

while True:
 print("1.add\n","2.sub\n","3.mul\n","4.div\n","5.Exit\n")
 choice =int(input("enter choice:"))
 if choice ==1:
   add()
 elif choice ==2:
    sub()
 elif choice ==3:
    mul()

 elif choice ==4:
    div()

 elif choice ==5:
   print("You Are Exit")

   break
 else:
    print("Invalid Choice")
