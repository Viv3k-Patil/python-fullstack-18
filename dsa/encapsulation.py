# class Employee:

#     def __init__(self,salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary
    
#emp = Employee(50000)

#print(emp.get_salary())

class Employee:

    def __init__(self, salary):
        self.__salary = salary   # private variable

    def get_salary(self):
        return self.__salary

emp = Employee(50000)

print(emp.get_salary())