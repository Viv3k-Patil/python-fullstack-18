balance = 10000

while True:

 print("1.  DEPOSIT"),
 print("2.  withdrwal"),
 print("3.  check balance"),
 print("4.  exit")

 choice =int(input("Please enter your choice: "))
 if choice == 1:
  balance = balance + int(input("Deposit amount :"))
  print("available balance",balance)

 elif choice == 2:
  with_amount = int(input("withdrwal amount: "))
  balance = balance - with_amount
  print("Available balance : ", balance)

 elif choice == 3:
  print("Available Balance:",balance )

 else:

  break   
   