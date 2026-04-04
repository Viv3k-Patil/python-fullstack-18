# list= [1,2,3,4,5,6,6,5,8]
# list.sort()
# slow=0
# fast =1
# length=len(list)
# while slow<length and fast<length:
#     if(list[slow]==list[fast]):
#         print(list[slow])
#         slow =fast+1
#         fast=slow+1
#     else:
#         slow+= 1
#         fast+=1


list=[5,3,1,5]
length=len(list) 
for i in range(len(list)): 
    for j in range(i+1,len(list)):
     if   list[i]==list[j]:
       print(i)
    

