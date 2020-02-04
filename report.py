from student import Student
import sqlite3

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/sullivanpierce/workspace/python/student-type-exercises/studentexercises.db"

    def create_student(self, cursor, row):
        return Student(row[1], row[2], row[3], row[5])

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


reports = StudentExerciseReports()
reports.all_students()
