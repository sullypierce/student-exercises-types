class Student:
    def __init__(self, first_name, last_name, slack_handle):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = ""
        self.exercises = list()

    def add_exercise(self, new_exercise):
        self.exercises.append(new_exercise)