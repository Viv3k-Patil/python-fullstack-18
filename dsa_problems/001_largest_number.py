# given a list, find the largest number in the list
# input_list = [1,5,66,8,78,19,22,36] 

input_list = [1,5,66,8,78,19,22,36]
# 78
big= 0
for num in input_list:
    if big < num:
        big = num

print(big)