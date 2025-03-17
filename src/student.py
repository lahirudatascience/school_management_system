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
    
    # Method to display common information
    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}"