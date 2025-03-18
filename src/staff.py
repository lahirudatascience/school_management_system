from person import Person

class Staff(Person):
    def __init__(self, name, age, address, staff_id, role, base_salary=30000, years_of_service=0, ssn=None):
        super().__init__(name, age, address, ssn)
        self.staff_id = staff_id
        self.role = role
        self.base_salary = base_salary  # Base salary of staff
        self.years_of_service = years_of_service  # Number of years worked
        self.calculated_salary = 0  # Initialize calculated salary


    # Overriding role_duties to define staff-specific responsibilities
    def role_duties(self):

        """
        Describe specific responsibilities for a Staff.

        """

        return f"Manages {self.role} tasks and supports school operations."
    
    def calculate_salary(self, bonus_per_year=1000):
        """
        Calculates the salary of the staff member based on their base salary and years of service.
        """
        self.calculated_salary = self.base_salary + (self.years_of_service * bonus_per_year)
        return self.calculated_salary

    def get_salary(self):
        """
        Returns the calculated salary of the staff member.

        """
        if self.calculated_salary == 0:
            raise ValueError("Salary has not been calculated yet.")
        return self.calculated_salary

    # Overriding display_info to include staff-specific details
    def display_info(self):
        return (
            f"{super().display_info()}\n"
            f"Staff ID: {self.staff_id}\n"
            f"Role: {self.role}\n"
            f"Base Salary: ${self.base_salary:.2f}\n"
            f"Years of Service: {self.years_of_service}\n"
            f"Total Salary: ${self.get_salary():.2f}"
        )
