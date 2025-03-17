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

    """
     Parameters:
        ssn (str, optional): The Social Security Number of the person. Defaults to None.
        Because ssn is private then we need to create a getter and setter method to access it
    """

    def __init__(self, name, age, address, ssn=None):
        self.name = name
        self.age = age
        self.address = address
        self.__ssn = ssn
    
    # Getter method for SSN
    def get_ssn(self):
        return self.__ssn
    
    # Setter method for SSN with validation
    def set_ssn(self, new_ssn):
        if isinstance(new_ssn, str) and len(new_ssn) == 9 and new_ssn.isdigit():
            self.__ssn = new_ssn
        else:
            raise ValueError("Invalid SSN format. SSN must be a 9-digit number.")
    
    # Method to display common information
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"