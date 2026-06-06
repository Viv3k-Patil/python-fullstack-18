# C - Create operation for files
# f = open("newtest2.txt", "w")
# f.write("Hello world!!")
# f.close()

# R - read file
# f = open("newtest2.txt", "r")
# data = f.read()
# print(data)
# f.close()

# U - update file
# case overwrite
# f = open("newtest.txt", "w")
# f.write("New content")
# f.close()

# case append
# f = open("newtest2.txt", "a")
# f.write("\nadded line")
# f.close()


# D - delete file
# import os
# if os.path.exists("newtest2.txt"):
#     os.remove("newtest2.txt")
# try:
#     os.remove("newtest2.txt")
# except FileNotFoundError:
#     print("file does not exist")

# using With
# with open("text.txt", "w") as file:
#     file.write("hello world!!")

# 1. Relative path create in current folder
# with open("new_file.txt", "w") as f:
#     f.write("hello world!!")

# # Absolute path
# with open("D:\softwares\python-fullstack-18\code\exception\my_file.txt", "w") as f:
#     f.write("hello world!!")    

# with open("D:\softwares\python-fullstack-18\code\exception\my_file.txt", "r") as f:
#     data = f.read()
#     print(data)

# create folder
# import os
# os.makedirs("created_file_handling", exist_ok=True)
# with open("created_file_handling/text.txt","w") as f:
#     f.write("hey there!!")


