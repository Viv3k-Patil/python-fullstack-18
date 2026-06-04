def cal_even_odd_num(num):
    if num%2 == 0:
     return "Even"
    else:
       return "Odd"
    
num = int(input("Enter number: "))


result_even_odd = cal_even_odd_num(num)
print(result_even_odd)