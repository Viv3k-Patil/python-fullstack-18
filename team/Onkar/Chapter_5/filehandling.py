# C - Create operation for files


# f = open ("newtest.txt", "w")
# f.write ("Hello Friends...!\n")
# f.write ("Hiiiiii...!")
# f.close()

# R - Read file

# f = open ("newtest.txt", "r")
# print(f.read())
# f.close

f = open ("newtest.txt", "r")
data = f.read()
print(data)
f.close()