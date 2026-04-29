
try:
    num = int(input("Please enter number : "))
    result = 10/num
    print("Result :",result)

except ZeroDivisionError:
    print("can not divided by zero...!")

except ValueError:
    print("Please enter valid number..")

finally:
    print("Program finished..!")