class Person:

    """
    Base class representing all people in the school
    """

    """
    Define common attributes 
        name (str): The name of the person.
        age (int): The age of the person.
        address (str): The address of the person.
    """

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        # Method to display common information
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"