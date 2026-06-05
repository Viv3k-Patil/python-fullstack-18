# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order
import itertools

l = [1,1,2,9,5,4]
m = [2,3,3,5,4,8,9,9]

# res=[1,2,3,4,5,8,9]

result = l+m
# print(list(set(result)))

a= []

b=[1,2]
c=[3,4]
# a = [*b, *c]
a = list(itertools.chain(b,c))

print(a)