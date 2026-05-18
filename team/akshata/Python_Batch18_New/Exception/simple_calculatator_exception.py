

try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    option = input("Enter operation (+,-,*,/): ")

    if option == "+":
        print("Result : ",num1 + num2)
    
    elif option == "-":
        print("Result : ",num1 - num2)

    elif option == "*":
        print("Result : ",num1 * num2)
    
    elif option == "/":
        print("Result : ",num1 / num2)

    else:
        print("Invalid operation")   

except ValueError:
    print("❌please enter valid number")

except ZeroDivisionError:
    print("❌ cannot divide by zero")

except Exception as e:
    print("❌ something went wrong..!", e)
 