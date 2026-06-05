# given a list [1,2,5,5,88,9,5,45]
# find second largest number in the list


list = [1,2,5,5,88,9,5,45]
list.sort()
second_largest_number = list[(-2)]
print(second_largest_number)




input_list = [1,2,5,5,88,9,5,45]
bignum = 0
second_big_val = 0
for each_num in input_list:
   temp = 0
   if bignum < each_num:
    bignum = each_num
    temp = second_big_val
    
print(second_big_val)