# simple calculator
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

#user have to choose which operation he want to perform
choice= int(input("Enter choice: "))
if choice == 1:
    print("Result: ", num1+num2)
elif choice == 2:
    print("Result: ", num1-num2)
elif choice == 3:
    print("Result: ", num1*num2)
elif choice == 4:
    print("Result: ", num1/num2)
else:
    print("Invalid option")            