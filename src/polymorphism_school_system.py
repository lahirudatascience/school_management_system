# main.py
from person import Person
from staff import Staff
from student import Student
from teacher import Teacher

def polymorphism_school_system():
    
    student = Student(name="Alice", age=15, address="123 School Lane", student_id="S12345")
    teacher = Teacher(name="Mr. Smith", age=40, address="456 Educator Road", employee_id="T98765", subject="Mathematics")
    staff = Staff(name="John Doe", age=35, address="789 Admin Street", staff_id="ST54321", role="Administrator", base_salary=35000, years_of_service=5)

    # Assign grades to the student
    student.assign_grades({"Math": 90, "Science": 85, "History": 88})
    
    # Mark attendance for the student
    student.mark_attendance("Math", True)
    student.mark_attendance("Math", False)
    student.mark_attendance("Science", True)
    student.mark_attendance("Science", True)

    # Schedule classes for the teacher
    teacher.schedule_classes({"Monday": "9:00 AM - 10:00 AM", "Wednesday": "11:00 AM - 12:00 PM"})

    # Calculate salary for the staff member
    staff.calculate_salary()

    # Store all individuals in a list (polymorphism in action)
    individuals = [student, teacher, staff]

    # Iterate through the list and call common methods
    for person in individuals:
        print("----------------------------------------")
        print(person.display_info())  # Calls the overridden display_info() method
        print(person.role_duties())   # Calls the overridden role_duties() method
        print("----------------------------------------")


polymorphism_school_system()