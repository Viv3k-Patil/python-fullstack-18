
#Stored correct username and password
username = "newgen"
password = "new123"

#take input from user, username and password
 
entered_username_input = input("Enter your username: ")
entered_userpassword_input  = input("Enter your password: ")

#compare stored credentials with user input
print(username == entered_username_input)
print(password == entered_userpassword_input)

#check if both username and password are correct
if username == entered_username_input and password == entered_userpassword_input:
    print("Login successfull")

else:
    print("Invalid credentials")