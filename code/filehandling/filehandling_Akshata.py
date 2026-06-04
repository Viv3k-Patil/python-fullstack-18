
#file create using open function()

file = open("new_file_creation.txt" , "w")
file.write("Hello Team, Welcome to python fullstack class")
file.close()


# CREATE
with open("New_file.txt", "w") as file:
    file.write("Hello World..!")


# READ

with open("New_file.txt", "r") as file:
   data = file.read()
   print(data)



# UPDATE




# DELETE