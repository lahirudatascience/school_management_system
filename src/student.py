from person import Person

class Student(Person):

    """
    Student class inheriting from Person
    Sub class representing a Student
    """

    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}  # Dictionary to store grades for subjects
        self.attendance_record = {}  # Dictionary to store attendance

    # Method to assign grades to subjects with validation
    def assign_grades(self, grades):
        try:
            if not grades:
                self.grades = {}  # If no grades are provided, default to an empty dictionary
                return
            for subject, grade in grades.items():
                if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
                    raise ValueError(f"Invalid grade {grade} for {subject}. Grade must be between 0 and 100.")
            self.grades = grades
        except ValueError as e:
            print(f"Error: {e}")
    
    # Method to calculate average grade
    def calculate_average(self):
        if not self.grades:
            return 0  # Default the average to 0 if no grades are assigned
        return sum(self.grades.values()) / len(self.grades)
    
    # Overriding role_duties to define student-specific responsibilities
    def role_duties(self):
        """
        Describe specific responsibilities for a student.

        Returns:
            str: A description of student responsibilities with name and student ID.
        """
        return f"{self.name} is a student with ID {self.student_id}. Their responsibilities include attending classes, and taking exams."
    
    # Method to track attendance
    def mark_attendance(self, subject, present):
        if subject not in self.attendance_record:
            self.attendance_record[subject] = []
        self.attendance_record[subject].append(present)

    # Method to display attendance summary
    def get_attendance_summary(self):
        summary = {}
        for subject, records in self.attendance_record.items():
            total_classes = len(records)
            attended_classes = sum(records)
            attendance_percentage = (attended_classes / total_classes) * 100 if total_classes > 0 else 0
            summary[subject] = f"{attended_classes}/{total_classes} ({attendance_percentage:.2f}%)"
        return summary 
    
    # Method to display common information
    def display_info(self):
        avg_grade = self.calculate_average()
        attendance_summary = self.get_attendance_summary()
        attendance_display = "\n".join([f"{subject}: {summary}" for subject, summary in attendance_summary.items()])
        
        return (
            f"{super().display_info()}\n"
            f"Student ID: {self.student_id}\n"
            f"Average Grade: {avg_grade:.2f}\n"
            f"Attendance Record:\n{attendance_display}"
        )