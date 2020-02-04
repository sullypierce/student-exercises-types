from student import Student
from cohort import Cohort
from exercise import Exercise
import sqlite3

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sullivanpierce/workspace/python/student-type-exercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

    def create_cohort(self, cursor, row):
        return Cohort(row[0])

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_student
            db_cursor = conn.cursor()
            

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.Name
            from Student s
            join Cohort c on s.cohort_id = c.Id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(f'{student.first_name} {student.last_name} is in {student.cohort}')

    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = self.create_cohort
            db_cursor = conn.cursor()
            

            db_cursor.execute("""
            SELECT Name
	        from Cohort
            order by Id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(f'{cohort.name}')


    def student_workload(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()
            

            db_cursor.execute("""
            SELECT 
                s.Id, 
                s.first_name, 
                s.last_name, 
                s.slack_handle, 
                c.Name, 
                e.Name ExerciseName,
                e.Id,
                e.language
	        from Student s
	        JOIN exercise_assignment ex ON s.Id = ex.student_id
	        JOIN Exercise e ON e.Id = ex.exercise_id
	        JOIN Cohort c ON s.cohort_id = c.Id
            """)

            all_students_with_exercises = db_cursor.fetchall()

            students = dict()
            print(all_students_with_exercises)
            for exercise_student in all_students_with_exercises:
                exercise_id = exercise_student[6]
                exercise_name = exercise_student[5]
                exercise_language = exercise_student[7]
                student_id = exercise_student[0]
                cohort_name = exercise_student[4]
                slack_handle = exercise_student[3]

                if student_id not in students:
                    # exercises[exercise_name] is adding a new key/value pair to the exercises dictionary, where exercise_name is the variable containing the key value which is string

                    # [student_name] is creating a list with one item, that item is the string contained in the variable student_name
                    new_student = Student(exercise_student[1], exercise_student[2], slack_handle, cohort_name)
                    students[student_id] = new_student
                    new_exercise = Exercise(exercise_name, exercise_language)
                    students[student_id].exercises[exercise_id] = new_exercise
                    print('this ran')
                else:
                    new_exercise = Exercise(exercise_name, exercise_language)
                    students[student_id].exercises[exercise_id] = new_exercise
                    print(new_exercise)
            for student in students:
                print(f'{students[student].first_name}:')
                for exercise in students[student].exercises:
                    print(f'\t* {students[student].exercises[exercise].name}')



reports = StudentExerciseReports()
reports.student_workload()
