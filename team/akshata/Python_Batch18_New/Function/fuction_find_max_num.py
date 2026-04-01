
#Write a function that takes two numbers and returns the greater number.

def find_max_num(num1,num2):
   if num1> num2:
      return num1
   elif num2 >num1:
     return num2
   else:
      return "Both are equals"
num1 = int(input("Enter First number: "))
num2 = int(input("Enter second number: "))
max_num = find_max_num(num1 , num2)
print("Greatest number is :",max_num)
