# User profile program.
# How to import a module
# how to look for documentation of a module,search for :  pypi [name of module]


import datetime  
# Import the datetime module to get the current year

# Get personal details from the user
name = input("Enter your name: ")  
# Ask user for their name and store it
yob = int(input("Enter your year of birth: "))  
# Ask birth year and convert to number
city = input("Enter your city: ")  
# Ask user for their city name
country = input("Enter your country: ")  
# Ask user for their country name
email = input("Enter your email: ")  
# Ask user for their email address
phone = input("Enter your phone number: ") 
 # Ask user for their phone number
profession = input("Enter your profession: ")  
# Ask user for their job or profession

# Calculate age using current year
current_year = datetime.datetime.now().year  
# Get the current year from today's date

age = current_year - yob  
# Calculate age by subtracting birth year from current year

# Display all user information
print("----- User Information -----")  
# Print a title with empty line before it
print("Name of user:", name)  
# Show the user's name
print("Age of user:", age)  
# Show the calculated age
print("Birth year of user:", yob)  
# Show the birth year entered
print("Current year:", current_year)  
# Show today's year
print("City of user:", city)  
# Show the user's city
print("Country of user:", country)  
# Show the user's country
print("Email of user:", email)  
# Show the user's email
print("Phone number of user:", phone) 
 # Show the user's phone number
print("Profession of user:", profession)  
<<<<<<< HEAD
# Show the user's profession
=======
# Show the user's profession


#write a program the addition of two number from user

num1 =int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
print("Addition of two numbers: ",sum)


#Take name and age from user

user_name = input("Please Enter Your Name : ")
user_age = input("Please Enter Your Age: ")

#print name and age 
print("Hello "+ user_name + ", you are "+ user_age + " years old")
>>>>>>> ea3141f4e13ba1afa5fb4513ad9ddaf7245c89d2
