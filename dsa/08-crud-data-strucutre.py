# lists
nums = [1,2,3,4,5,6,7,8]

result = []

for num in nums:
    if num not in result:
       result.append(num)

    print(result)

nums2 = [10,20,60,34,55,38,89,71]

nums2.sort()

print("second largest nums:",nums2[-2])

# tuple
data = (1,3,4,6,3,4,8,2)

print(data.count(3))

data2 = (10,20,30)

temp = list(data2)

temp.append(40)

data2 = tuple(temp)

print(data2)

# set


# dict