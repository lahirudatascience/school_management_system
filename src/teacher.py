from person import Person

class Teacher(Person):

    """
    Teacher class inheriting from Person
    Sub class representing a Teacher
    """

    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
    
    def display_info(self):
        # Method to display common information
        return f"{super().display_info()}, Employee ID: {self.employee_id}, Subject: {self.subject}"
