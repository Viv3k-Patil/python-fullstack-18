#User input based signal Workflow

# def signal_colour(signal):

#     if signal == "Red":
#         print("Stop")

#     elif signal == "Yellow":
#         print("Wait")

#     elif signal == "Green":
#         print("GO")

#     else:
#         print("Invalid signal")


# while True:

#    user_input = (input("Enter signal (Red/Yellow/Green/Exit ): "))
#    if user_input == "exit":
#        print("Program stopped")
#        break

#    signal_colour(user_input)


while True:
    print("\n1. Red")
    print("2. Yellow")
    print("3. Green")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
      print("STOP")

    elif choice == 2:
      print("WAIT")

    elif choice == 3:
      print("GO")

    elif choice == 4:
      print("Program Exit")

      break
    
    else: 
      print("invalid choice ")