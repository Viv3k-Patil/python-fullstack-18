#Write a function that prints all even numbers from a given list.


def cal_even_num_list(given_list):
   even_list =[]
   for num in given_list:
    if num %2 == 0:
      even_list.append(num)
   return even_list
   

given_list = [1,2,3,4,5,6,7,8,9,10]
even_list =cal_even_num_list(given_list)
print(even_list)