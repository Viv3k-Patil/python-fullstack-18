#remening_course_perc= 96

#complete_course_perc= 100 - remening_course_perc
#print(f"{complete_course_perc}% of the course is complete")

#ATM 
import pyfiglet
balance=2000

print("WELCOME TO ATM")
user_name=input("enter your name:")
print(pyfiglet.print_figlet(user_name))

print("1.bank balance")
print("2.withdraw")
print("3.deposite")
print("4.Exit")

action=input("Enter your action")

if action=="1":
    print("Your balance is:",balance)
elif action=="2":
   print("You have select withdraw:")
   withdraw=int(input("enter amount to withdraw:"))
    
   if withdraw<balance:
       
        newbalance=(balance - withdraw)
        balance=newbalance
        print("your new balance is:",balance)
   else:
         print("Insufficent balance")
         
elif action=="3": 
     print("You have select Deposite:")
deposite=int(input("enter amount"))
new_deposite=int(balance)+int(deposite)
print(new_deposite)


   
 
   