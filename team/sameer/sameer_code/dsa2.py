# given a list [1,2,5,5,88,9,5,45]
# find second largest number in the list
# list=[1,2,5,5,88,9,5,45]
# list2=sorted(list)
# print(list2[-2])

list=[1,2,3,4,5,6,8,7]
big=0
sec=0
for i in list:
   sec = big
   if i>big:
      big=i
print(big)
print(sec)