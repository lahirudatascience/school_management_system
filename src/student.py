from person import Person

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    
    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}"