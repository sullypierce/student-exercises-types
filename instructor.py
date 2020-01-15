from student import Student

class Instructor:
    def __init__(self, first, last, handle, specialty):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = ""
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        if self.cohort == student.cohort:
            student.add_exercise(exercise)
        else:
            print("That student is not in your cohort")