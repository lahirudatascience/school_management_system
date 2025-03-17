from student import Student
from teacher import Teacher
from staff import Staff

# Creating instances of each class
student = Student("Alice", 15, "123 Main St", "S1001")
teacher = Teacher("Mr. Smith", 40, "456 Elm St", "T2001", "Mathematics")
staff = Staff("Mrs. Johnson", 50, "789 Oak St", "ST3001", "Administrator")

# Printing information for each object
print(student.display_info())
print(teacher.display_info())
print(staff.display_info())