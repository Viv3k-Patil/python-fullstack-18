# Stored correct username and password
username = "newgen"
password = "new123"

# Take input from user
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Check if username and password match
if username == entered_username and password == entered_password:
    print("Login successful")
else:
    print("Invalid credentials")