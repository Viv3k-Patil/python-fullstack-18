### AGES 

age=int(input("enter your age:"))

if age<=18:
    print("You Are Minor")

elif age>=18 and age<=35:
    print("You Are Adult")

elif age>=35 and age<=60:
    print("You Are senior")

else:
    print("Your Are Senior Citizen")