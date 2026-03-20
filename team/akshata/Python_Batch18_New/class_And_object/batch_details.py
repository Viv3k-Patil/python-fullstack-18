
class Batch():

    def __init__(self,
                 batch_name,
                 batch_number,
                 batch_timings,
                 instructor,
                 student_list
                 ):

        self.batch_name = batch_name
        self.batch_number = batch_number
        self.batch_timings = batch_timings
        self.instructor = instructor
        self.student_list = student_list
 
    def __str__(self):
        return f"batch name: {self.batch_name},\nbatch number:{self.batch_number},\nbatch timinges: {self.batch_timings},\ninstructor{self.instructor},\nstudent list:{self.student_list}"

a = Batch(
    "Python-fullstack-18",
     18,
    "7.30am - 9.30am",
    "vivek- patil",
    [
        "Akshata",
        "sameer",
        "Rushikesh",
        "Parth"
    ]
)

print(a)