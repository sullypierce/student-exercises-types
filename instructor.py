from student import Student
from nss_person import Nss_person

class Instructor(Nss_person):
    def __init__(self, first, last, handle, specialty):
        super().__init__(first, last, handle)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        try:
            if self.cohort == student.cohort:
                student.add_exercise(exercise)
            else:
                print("That student is not in your cohort")
        except AttributeError:
            print(f"this instructor is not assigned to a cohort")