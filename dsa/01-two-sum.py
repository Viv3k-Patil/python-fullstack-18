
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# target = 12
# a = [2,9,8,4,7,5,6]
#      0,1,2,3,4,5,6
# output = [2,3]


target = 12
a = [2,9,8,4,7,5,6]
n = len(a)
ans = []
for i in range(n):
    for j in range(i+1, n):
        if a[i]+a[j]==target:
            ans.append([i,j])

print(ans)

# print only single list and stop the loop.



