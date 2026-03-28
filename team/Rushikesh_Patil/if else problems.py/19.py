##19. Write a Python program to check if a student's attendance is greater than 75%.

total_class=int(input("Enter Your Classes:"))
attende_class=int(input("Enter Your Attend Classes:"))
total_percentage=(total_class/attende_class)*100
if total_percentage>75:
    print("percentage greater than 75%")
else:
    print("percentage less than 75%")
