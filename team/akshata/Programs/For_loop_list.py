#Write a program using in for loop

a = [10,20,30,40,50]

for num in a:
    print(num)


#add all the number in the list

num_list = [20,40,60,80,100]
sum = 0
for num in num_list:
    sum = sum + num
    print(sum)

print("------ SUM of Even Number list -------")
#write a program sum of even number in the list
num_new_list = [1,2,3,4,5,6,7,8,9,10]
sum_of_even = 0

for i in num_new_list:
    if  i%2 == 0:
        sum_of_even = sum_of_even + i
        print(i,"=",sum_of_even)


print("-----SUM of ODD number List -----")
#write a program sum of odd number in the list
num_new_list = [1,2,3,4,5,6,7,8,9,10]
sum_of_even = 0

for i in num_new_list:
    if not i%2 == 0:
        sum_of_even = sum_of_even + i
        print( sum_of_even)

  