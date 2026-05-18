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
        return f"student: {self.name},\nage: {self.age},\npassout_year {self.passout_year},\n"
    