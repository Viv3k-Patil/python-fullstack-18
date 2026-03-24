
# given a list, find the largest number in the list
# input_list = [1,5,66,8,78,19,22,36] 

input_list = [1,5,66,8,78,19,22,36]
largest = input_list[0]
for num in input_list:
    if num > largest:
        largest = num
print("Largest number is : ",largest)


numbers = [1,5,66,8,78,19,22,36]
largest_num = max(numbers)
print("Largest number is :",largest_num)



num_list = [1,5,66,8,78,19,22,36]
largest_number = 0
for i in num_list:
    if largest_number < i:
        largest_number = i
print("Largest number in the list:",largest_number)