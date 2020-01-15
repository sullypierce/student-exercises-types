class Cohort:
    def __init__(self, name):
        self.name = name
        self.students = list()
        self.instructors = list()

    def add_student(self, new_student):
        new_student.cohort = self.name
        self.students.append(new_student)
        
    
    def add_instructor(self, new_instructor):
        new_instructor.cohort = self.name
        self.instructors.append(new_instructor)
