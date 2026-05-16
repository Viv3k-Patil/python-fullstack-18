
# print("hello")
# reading file throws error as no such file exists.it only reads existing file
# file = open("new_text.txt","r")
# file.read()
# print("the file has been read")
# file.close()


##new file is created and data is added
# file = open("new_text.txt","w")
# file.write("now i am reading the file")
# print("the above file haas been created")
# file.close()


##file is overwritten
# file = open("new_text.txt","w")
# file.write("now i am reading the file \n what is my next action")
# print("the above file haas been overwritten")
# file.close()


## for append we write file.write as append is used in class method
# file = open("new_text.txt","a")
# file.write("\n all the information should be capital letters")
# print("the file got appended")
# file.close()

##will get an error as the file new_text.tx already exits
# file = open("new_text.txt","x")
# file.write("let me see if new file is created")
# print("new file is created")
# file.close()

##giving new file name to create
# file = open("new_textfile.txt","x")
# file.write("let me see if new file 1 is created")
# print("new file is created")
# file.close()

##creating file using with
# with open("new_text.txt","r") as file:
#     file.read()
#     print("file read only")

##creating/over written file using with
# with open("new_text.txt","w") as file:
#     file.write("write access has been given to the file")
#     print("file write only")

##append with write
# with open("new_text.txt","a") as file:
#     file.write("\n new line added")
#     print("new line added succesfully")

##deleting the file

import os
# if os.path.exists("new_text.txt"):
#     os.remove("new_text.txt")
#     print("file deleted successfully")
# else:
#     print("file not found")

##new folder created
#os.makedirs("data",exist_ok=True)

##new file inside data folder is created
# with open("data/new_text.txt","w") as file:
#     file.write("new file inside data folder is created")
#     print("file created successfully")

##list files
# files = os.listdir("data")
# print(files)

##exception handling using with
##creating a new file
# def create_file(name, content):
#     with open(name,"w") as file:
#         file.write(content)
#         print("created")


# create_file("new_file.txt","hey there")


## reading the created file
# def read_file(name):
#     with open(name,"r") as file:
#         return file.read()
# print("read access given")
    
    

# read_file("new_textfile.txt")

##update the created file using function
# def create_file(name, content):
#     with open(name,"w") as file:
#         file.write(content)
#         print("file is updated successfully")


# create_file("new_file.txt","hey there,file is updated")

##deleting the txt file using function


# try:
#     def delete_file(name):
#     if os.path.exists(name):
#         os.remove(name)
#     print("file has been deleted")
# except:

# delete_file("new_file.txt")