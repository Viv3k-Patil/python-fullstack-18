balance = 5000

print("Welcome to ATM")

print("1 Check Balance")
print("2 Withdraw Money")
print("3 Deposit Money")
print("4 Exit")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Transaction successful")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance")

elif choice == 3:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("Money deposited")
    print("New balance:", balance)

elif choice == 4:
    print("Thank you for using ATM")

else:
    print("Invalid option")