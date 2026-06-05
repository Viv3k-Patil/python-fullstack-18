#Q1. Check Positive or Negative

#Write a function to check whether a number is positive, negative, or zero.

def check_num_pos_neg(num):
    if num > 0:
        return "This is postive number ",num
    elif num < 0:
        return "this is Negative number ",num
    else:
        return "Zero"

num = int(input("Please enter a number: "))
check_num = check_num_pos_neg(num)
print(check_num)