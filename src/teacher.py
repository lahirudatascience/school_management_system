from person import Person

class Teacher(Person):

    """
    Teacher class inheriting from Person
    Sub class representing a Teacher
    """

    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject # Subject the teacher specializes in
        self.class_schedule = {}  # Dictionary to store class schedules

    # Overriding role_duties to define teacher-specific responsibilities
    def role_duties(self):
        """
        Describe specific responsibilities for a Teaches.

        Returns:
            str: A description of Teaches responsibilities with subject.
        """
        return f"Teaches {self.subject}, prepares lessons, and evaluates students."
    
    # Method to assign a class schedule
    def schedule_classes(self, schedule):
        """
        Assign a class schedule for the teacher.
        """
        self.class_schedule = schedule
        print(f"Class schedule updated for {self.name}: On {', '.join(self.class_schedule.keys())}")    
    
    # Method to display common information
    def display_info(self):
        return f"{super().display_info()}, Employee ID: {self.employee_id}, Subject: {self.subject}"
