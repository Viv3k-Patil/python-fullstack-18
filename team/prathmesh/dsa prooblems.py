#bubbble sort
#def bubble_sort(arr):
   # n=len(arr)
    #for i in range(n):
    #    for j in range(0,n-i-1):
   #         if arr[j]>arr[j + 1]:
  #              arr[j],arr[j + 1]= arr[j+1] ,arr[j]
 #   return(arr)

#my_list=[64,34,25,12,22,11,90]
#print(bubble_sort(my_list))


#a=2
#b=10
#c=30

#sum=a+b
#avg=0
#if c>avg: 
  #  avg=sum/2
 #   print("c is greter")


#list=[1,2,3,4,5,6]

#list.append(7)
#list.remove(5)
#print(list[1])
#print(list)

#lenear search

#def array(arr,target):
    #for i in range(len(arr)):
    #    if arr[i]==target:
   #      return i
  #  else:
        
 #       return -1
    
    
        
#print(array([10,15,42,65,32],11))


# def binary_search(arr,target):
#     left,right=0,len(arr)-1

#     while left<=right:
#         mid= (left + right) // 2

#         if arr[mid]==target:
#            return mid
#         elif arr[mid]<target:
#             left=mid+1
#         else:
#             right=mid-1    
                 
# print(binary_search([1,2,3,4,5],4))    

#check if Array is Sorted

# def is_arr_sorted(arr):
#     for i in range (len(arr)-1):
#         if arr[i]>arr[i+1]:#“Check if the current element is greater than the next element”
#             return False
#         else:
#             return True

# print(is_arr_sorted([1, 2, 3, 4])) 
# print(is_arr_sorted([3,1,5]))

# def sort_arr(arr,value):
#     arr.append(value)
#     arr.remove(value)
#     arr.sort()
#     return arr
# print(sort_arr([5,3,2,1],4))    


#Merge Two Sorted Arrays

# def merge_sort(arr1,arr2):
#     i=j=0
#     result=[]

#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1

#         result.extend(arr1[i:]) 
#         result.extend(arr2[j:])   

#         return result
        

# print(merge_sort([1,3,5],[2,4,6]))                

# def mergr_sort(arr1,arr2):
#     i=j=0
#     result=[]
#     while i<len(arr1) and j<len(arr2):
#             if arr1[i]<arr2[j]:
#                 result.append(arr1[i])
#                 i +=1
#             else:   
#                result.append(arr2[j])
#                j +=1     

#                result.append(arr1[i:])
#                result.append(arr2[j:])

#                return result
       
# print(mergr_sort([1,3,5,7,9],[2,4,6,8,10]))     


# class Acount:
#     def __init__(self,account_number):
#         #data store
#       self.account_number=account_number
#       self.balance =0

# a=Acount(1234569)
# print(a.balance)
         
# table1=["x","-","-"]
# table2=["-","x","-"]
# table3=["-","-","x "]

# print("|".join(table1))
# print("|".join(table2))
# print("|".join(table3))

board= [
    ["x","",""],
    ["","x",""],
    ["","","x"]
]
for row in board:
  for col in row:
    print(col)
