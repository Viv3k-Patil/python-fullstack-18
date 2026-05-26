
#given list input_list = [1,2,3,4,5,6,6,5,8,1]

# input_list = [1,2,3,4,5,6,6,5,8,1]

# input_list.sort()

# slow = 0
# fast = 1
# length = len(input_list)

# while slow < length and fast < length:
#    if input_list[slow] == input_list[fast]:
#       print(input_list[slow])
#       slow = fast+ 1
#       fast = slow+ 1

#    else:
#       slow+= 1
#       fast+= 1

# print("*******-------------------***********")
     
# list = [1,9,2,8,3,9,5,1,3,5,7]

# list.sort()

# pointer1 = 0
# pointer2 = 1

# length1 = len(list)

# while pointer1< length1 and pointer2 < length1:
#    if list[pointer1] == list[pointer2]:
#       print(list[pointer1])
#       pointer1 = pointer1 + 2
#       pointer2 = pointer2 + 2
#    else:
#       pointer1+= 1
#       pointer2+= 1

# list = [1,9,2,8,3,9,1]
# list.sort()
# seen = []
# duplicate = []

# for i in list:
#    if i not in seen:
#       seen.append(i)
#    else:
#       duplicate.append(i)
   
# print(duplicate)


#list = [1,9,2,8,3,9,1]

duplicate = []

#for i in list:
#   if list.count(i)> 1 and i not in duplicate:
 #     duplicate.append(i)

#print(duplicate)


l = [1,1,2,9,5,4]
m = [2,3,3,5,4,8,9,9]

result =list(set(l + m))
print(result)
    
    
l.extend(m)  
print(list(set(l)))
    
