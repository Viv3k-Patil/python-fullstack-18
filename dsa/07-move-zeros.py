# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

nums = [1,0,3,0,5,6,0]
result = []
# output [1,3,5,6,0,0,0] order maintain, same list
# print(sorted(l, reverse=True))
for num in nums:
    if num != 0:
        result.append(num)


for i in range(len(nums)-len(result)):
    result.append(0)


# O(n)
# s=0
# f=0
# n=len(nums)

# while f<n:
#     if nums[f]!=0:
#         nums[s], nums[f]=nums[f], nums[s]
#         f+=1
#         s+=1
#     else:
#         f+=1

# O(n) time complexity

print(nums)
print(result is result)
print(result)
