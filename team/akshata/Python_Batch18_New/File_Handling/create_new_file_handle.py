
# reading file throws error file not found 

# file = open("new_text.txt", "r")
# file.read()
# print("Hello World..!")
# file.close()

# create new file using write mode
# file = open("new_text.txt", "w")
# file.write("This file has been created..!")
# print("File is created successfully.")
# file.close()


# overwrite the file using write mode
# file = open("new_text.txt", "w")
# file.write("This file has been created..!\n added some new lines")
# print("File is created successfully and overwrite the file.")
# file.close()

# for append mode using file.write mode to add new line in last 
# file = open("new_text.txt", "a")
# file.write("\nNew line addedd")
# print("Append some program in new_text file.")
# file.close()


#x = Create new file (error if exists)
# file = open("new_text1.txt", "x")
# file.write("This is new file")
# file.close()

#using with 

#Read

# with open("new_text.txt", "r") as file:
#     file.read()
#     print("file read only..!")


#write
# with open("new_text.txt", "w") as file:
#     file.write("Hello Friends.. How are you? ")
#     print("file read only..!")

#append

# with open("new_text.txt", "a") as file:
#     file.write("\n New line added")
#     print("New line added successfully")


#Delete mode - creating deleted file

import os

# if os.path.exists("new_text.txt"):
#    os.remove("new_text.txt")
#    print("file deleted successfully..")
# else:
#    print("File not found...!")


#New folder is created = data
# os.makedirs("data", exist_ok= True)


#file is created inside data folder
# with open("data/new_text.txt", "w") as file:
#     file.write("file created inside folder...")
#     print("File created succssfully...")

# list of folder
# files = os.listdir("data")
# print(files)


# using def function 
#create file

# def create_file(name , content):
#     with open(name , "w") as file:
#         file.write(content)

# create_file("demo.txt", "Hello Team")
# print("File created successfully")

#read file
# def read_file(name):
#     with open(name , "r") as file:
#      return file.read()
    
# read_file("demo.txt")
# print("Only read file demo.txt")


#update file

# def update_file(name, new_content):
#    with open(name, "w") as file:
#     file.write(new_content)

# update_file("demo.txt","\nAdd new line")
# print("Updated successfully...")

#delete file

# def delete_file(name):
#     try:
#       os.path.exists(name)
#       os.remove(name)
#     except FileNotFoundError:
#        print("File not found")

# delete_file("demo.txt")
# print("File deleted succsully done...")

