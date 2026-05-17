input_list = [1,2,3,4,5,6,6,5,8,1]
input_list.sort()
print(input_list)
duplicates = []
for num in input_list:
    if input_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(duplicates)