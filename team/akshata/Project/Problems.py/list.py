
# 1. Write a Python program to print all elements of a list one by one.
# Input:
# [10, 20, 30, 40]
# Output:

# 10  
# 20  
# 30  
# 40


#Solution

# input = [10,20,30,40]

# for i in input:
#     print(i)


# 2. Write a Python program to calculate the sum of all numbers in a list (without using sum()).
# Input:
# [1, 2, 3, 4, 5]
# Output:
# 15
   
#solution
# input = [1,2,3,4,5]
# count = 0
# for i in input:
#     count = count + i
# print("Sum of given list:" ,count)



# 3. Write a Python program that counts how many even numbers are in a list.
# Input:
# [10, 13, 16, 17, 20]
# Output:
# 3

# input = [10, 13, 16, 17, 20]
# count = 0
# for i in input:
#    if i % 2 == 0:
#       count += 1
# print("Even number count: ",count)


# 3. Write a Python program that counts how many odd numbers are in a list.
# Input:
# [10, 13, 16, 17, 20,4,7]
# Output:
# 

# list = [10, 13, 16, 17, 20, 4, 7]

# count = 0

# for i in list:
#    if not i%2 == 0:
#     count += 1
# print(count)
      

#Write a program  to give a list of count

# list = [10, 13, 16, 17, 20, 4, 7]
# count = 0
 
# for i in list:
#     count += 1
# print(count)

# 4. Write a Python program to find the largest number in a list (without using max()).
# Input:
# [12, 45, 2, 99, 18]
# Output:
# 99

# list = [12, 45, 2, 99, 18]
# largest_num = 0
# for i in list:
#     if i > largest_num:
#         largest_num = i
# print(largest_num) 


# 5. Write a Python program that reverses a list using a loop (not using reverse() or slicing).
# Input:
# [1, 2, 3, 4, 5]
# Output:
# [5, 4, 3, 2, 1]

# list = [1, 2, 3, 4, 5]
# list.reverse()

# print(list)

# list = [1, 2, 3, 4, 5] 
# i = len(list)-1
# while i >= 0:
#     print(list[i], end = " ")
#     i-= 1


# 6. Write a Python program that removes all occurrences of a specific number from a list.
# Input:
# List: [1, 2, 3, 2, 4, 2], Number: 2
# Output:
# [1, 3, 4]


list = [1, 2, 3, 2, 4, 2]
result = []
for i in list:
    if i !=2:
        result.append(i)
print(result)