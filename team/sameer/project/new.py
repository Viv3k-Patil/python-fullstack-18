
class Student:
    def __init__(
        self,
        name,
        age,
        passout_year,
        is_current_course_completed,
        courses_taken,
        is_fee_paid,
        applied_for_job,
        interviews_given
        ):
            self.name = name
            self.age = age
            self.passout_year = passout_year
            self.is_current_course_completed = is_current_course_completed
            self.courses_taken =courses_taken
            self.is_fee_paid=is_fee_paid
            self.applied_for_job=applied_for_job
            self.interviews_given=interviews_given
    def __str__(self):
        return f"student: {self.name}"
class Batch:
    # class body starts
    def __init__(self, 
    batch_name, 
    batch_number,
    batch_timings,
    instructor,
    student_list,

    ):
        self.batch_name = batch_name
        self.batch_number = batch_number
        self.batch_timings = batch_timings
        self.instructor = instructor
        self.student_list = student_list
    
    def __str__(self):
        return f"batch_name: {self.batch_name}, \nbatch_number: {self.batch_number}, \nbatch_timings: {self.batch_timings} \ninstructor: {self.instructor} \nstudents: {self.student_list}"
    
    def greet(self):
        print("you are using class Batch")
        
    def get_student_list(self):
        return self.student_list
    
    def add_new_student(self, student_name):
        self.student_list.append(student_name)
        return student_name
        
    def get_student_count(self):
        return len(self.student_list)
    # class body ends
    
s1 = Student(
        "Newly adddedd student",
        25,
        2020,
        False,
        ["python","java"],
        True,
        True,
        10
        )
# print(s1)

# s2 = Student(
#         "New Student 2",
#         25,
#         2020,
#         False,
#         ["python","java"],
#         True,
#         True,
#         10
#         )
# print(s2)







a = Batch(
        "python-ffullstack-18",
        18,
        "7.30am - 9.30am",
        "Vivek Patil",
        [
            "Girish",
            "Sameer",
            "Akshada",
            "Rushikesh"
        ]
    )

a.add_new_student(s1)
student_list_batch18 = a.get_student_list()
for each_student in student_list_batch18:
    print(each_student)

# # a.greet()
# # print(a.get_student_list())
# a.add_new_student("PQR")
# print(a)
# b = Batch(
#         "MERN-fullstack-22",
#         22,
#         "7.30pm - 9.30pm",
#         "XYZ",
#         [
#             "Girish",
#             "Sameer",
#             "Akshada",
#             "Rushikesh"
#         ]
#     )

# a.instructor = "XYZ"
# print(a.instructor)
# print(a)
# print(a.)
# print(a.batch_name)
# print(a.batch_number)

# b = Batch("Java-fullstack-batch", 31)
# print(b.batch_name)
#print(b.batch_number)