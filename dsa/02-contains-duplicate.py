#Given an integer array nums, 
#return true if any value appears at least twice in the array, and return false if every element is distinct.

a=[1,2,3,4,5,6,5,4,7]
n = len(a)

# # 
# for i in range(n):
#     for j in range(i+1, n):
#         if a[i]==a[j]:
#             print("duplicate")


# rushikesh 
# for i in range(len(a)):
#     if a.count(a[i])>1:
#         print("duplicate")


# set O(1) O(n)
if len(a)!=len(set(a)):
    print("duplicate")
