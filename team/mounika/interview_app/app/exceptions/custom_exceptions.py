
class InterviewNotFoundException(Exception):
    def __intit__(self,interview_id: int):
        self.interview_id = interview_id