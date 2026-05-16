

class InterviewNotFoundException(Exception):
    def __init__(self,interview_id : int):
        self.interview_id = interview_id
        self.msg = f" interview now found with id {interview_id}"
        super().__init__(self.msg)

