# given a list [1,2,5,5,88,9,5,45]
# find second largest number in the list
# 45

input_list = (1,2,5,6,88)
# bignum = 0
# for each_num in input_list:
#     # code block start
#     if bignum<each_num:
#         bignum=each_num
#     #code block end

# print(bignum)
# input_list.sort()
# print(input_list[-2])
bigval=0
secondbigval=0
for each_val in input_list:
    temp = bigval
    if bigval<each_val:
        bigval=each_val
        secondbigval=temp

print(secondbigval)