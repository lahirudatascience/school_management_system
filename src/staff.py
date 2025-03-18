from person import Person

class Staff(Person):
    def __init__(self, name, age, address, staff_id, role):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.role = role

    # Overriding role_duties to define staff-specific responsibilities
    def role_duties(self):

        """
        Describe specific responsibilities for a Staff.

        Returns:
            str: A description of Staff responsibilities with role.
        """

        return f"Manages {self.role} tasks and supports school operations."
    
    def display_info(self):
        return f"{super().display_info()}, Staff ID: {self.staff_id}, Role: {self.role}"