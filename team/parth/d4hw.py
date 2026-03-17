# Write program:
# Take 2 numbers from user
# Add them
# Print result
# Try causing TypeError intentionally.
# Fix it.

# Intentional TypeError
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = num1 + num2

print("Addition is:", result)
#This happens because Python concatenates strings instead of adding numbers.

#Fixed TypeError
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2

print("Addition is:", result)