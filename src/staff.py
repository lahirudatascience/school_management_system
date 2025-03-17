from person import Person

class Staff(Person):
    def __init__(self, name, age, address, staff_id, role):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.role = role
    
    def display_info(self):
        return f"{super().display_info()}, Staff ID: {self.staff_id}, Role: {self.role}"