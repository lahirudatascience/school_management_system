from student import Student
from teacher import Teacher
from staff import Staff

#Question 01 Example Task a
# Creating instances of each class
student = Student("Alice", 15, "123 Main St", "S1001")
teacher = Teacher("Mr. Smith", 40, "456 Elm St", "T2001", "Mathematics")
staff = Staff("Mrs. Johnson", 50, "789 Oak St", "ST3001", "Administrator")

# Printing information for each object
print(student.display_info())
print(teacher.display_info())
print(staff.display_info())


#Question 01 Example Task b
student = Student("Alice", 15, "123 Main St", "S1001")
student.assign_grades({"Math": 85, "Science": 90, "English": 78})  # Valid grades
print(student.calculate_average())
# student.assign_grades({"History": 110})  # Invalid grade example
student.assign_grades({})  # No grades assigned, should default to average = 0
print(student.calculate_average())


#Question 01 Example Task c
# Trying to update SSN with setter method
try:
    student.set_ssn("987654321")
    print("Updated Student SSN:", student.get_ssn())
except ValueError as e:
    print(e)