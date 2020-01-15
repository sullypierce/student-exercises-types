from student import Student
from exercise import Exercise
from cohort import Cohort
from instructor import Instructor

#create exercises
exercise1 = Exercise("do something", "python")
exercise2 = Exercise("do anything", "python")
exercise3 = Exercise("make something", "python")
exercise4 = Exercise("make anything", "python")

#create cohorts
cohort36 = Cohort("Cohort 36")
cohort35 = Cohort("Cohort 35")
cohort37 = Cohort("Cohort 37")

#create students
ryan1 = Student("Ryan", "Cunningham", "rc1")
ryan2 = Student("Ryan", "Bishop", "rb1")
ryan3 = Student("Ryan", "Crawley", "rc2")
sullivan = Student("Sully", "Pierce", "sp1")

#assign students
cohort36.add_student(ryan1)
cohort36.add_student(ryan2)
cohort36.add_student(ryan3)
cohort36.add_student(sullivan)


#create instructors
joe = Instructor("Joe", "Shepherd", "js1", "funny")
jisie = Instructor("Jisie", "David", "jd1", "good at instructing")
jenna = Instructor("Jenna", "not sure", "jn1", "teaching")

#assign instructors
cohort36.add_instructor(joe)
cohort36.add_instructor(jisie)
cohort36.add_instructor(jenna)

#assign exercises
joe.assign_exercise(ryan1, exercise1)
joe.assign_exercise(ryan1, exercise2)
jisie.assign_exercise(ryan2, exercise2)
jisie.assign_exercise(ryan2, exercise3)
jenna.assign_exercise(sullivan, exercise3)
jenna.assign_exercise(sullivan, exercise4)
joe.assign_exercise(ryan3, exercise1)
joe.assign_exercise(ryan3, exercise2)

print(ryan1.cohort)

cohort36.list_student_exercises()
 


