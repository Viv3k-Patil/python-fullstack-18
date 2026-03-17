 #this is bank project 
balance= 10000
while True:
 print("Enter your choice\n 1.DEPOSIT\n 2.WITHDRWAL\n 3.CHECK BALANCE\n 4.EXIT")
 choice=int(input("choice "))
 if choice == 1:
    print("enter deposit amount")
    balance= balance+int(input(""))
    print("available balance = ",balance)
 elif choice==2:
    print("enter withdrwal amount")
    balance= balance-int(input(""))
    print("available balance = ",balance)
 elif choice==3:
    print("available balance is ",balance)
 else :
    break