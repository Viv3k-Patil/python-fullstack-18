
print("__________*****EMPLOYEE DETAIL MANAGEMENT SYSTEM**********")

employees = []

while True:

    print("\n1. Add Employee")
    print("2. Display Employee")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        emp_department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employee = {
            "ID": emp_id,
            "Name": emp_name,
            "Department": emp_department,
            "Salary": salary
        }

        employees.append(employee)
        print("Employee Added Successfully")

    elif choice == 2:
        for emp in employees:
            print("ID:", emp["ID"])
            print("Name:", emp["Name"])
            print("Department:", emp["Department"])
            print("Salary:", emp["Salary"])
            print("----------------------")

    elif choice == 3:
        search_id = input("Enter Employee ID to Search: ")
        for emp in employees:
            if emp["ID"] == search_id:
                print("Employee Found")
                print("ID:", emp["ID"])
                print("Name:", emp["Name"])
                print("Department:", emp["Department"])
                print("Salary:", emp["Salary"])
                break

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice. Please Try Again.")
    