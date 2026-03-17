### ATM PROJECT

print("WELCOME TO THE ATM MACHINE")

print("INSERT YOUR CARD")

pin = int(input("ENTER YOUR PIN: "))
print("YOUR PIN IS:", pin)


print("ENTER YOUR CHOICE")


print("1. CHECK BALANCE")
print("2. WITHDRAW MONEY")
print("3. DEPOSIT MONEY")
print("4. EXIT")


balance=100000
choice=(input("ENTER YOUR CHOICE: "))



if choice==1:
    print("YOUR BALANCE IS:",balance)




elif choice==2:
    print("ENTER THE WITHDRAW AMOUNT")
    withdraw_amount=int(input())
    if withdraw_amount>balance:
        print("INSUFFICIENT BALANCE")
    else:
        balance=balance-withdraw_amount





elif choice==3:
    print("ENTER THE DEPOSIT AMOUNT")
    deposit_amount=int(input())
    balance=deposit_amount+balance
    print("YOUR NEW BALANCE IS:",balance)







elif choice==4:
    print("THANK YOU FOR USING THE ATM MACHINE")

