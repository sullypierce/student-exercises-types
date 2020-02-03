from nss_person import Nss_person

class Student(Nss_person):
    def __init__(self, first_name, last_name, slack_handle):
        super().__init__(first_name, last_name, slack_handle)
        self.exercises = list()

    def add_exercise(self, new_exercise):
        self.exercises.append(new_exercise)

    def list_exercises(self):
        exercise_string = ""
        for exercise in self.exercises:
            exercise_string += exercise.name
            
            if self.exercises.index(exercise) == (len(self.exercises)-2):
                exercise_string += ", and "
            elif self.exercises.index(exercise) < (len(self.exercises)-1):
                exercise_string += ", "
            else:
                exercise_string += "."
        print(f"{self.first_name}  is working on {exercise_string}")