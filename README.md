# School Management System - README

## Overview

The School Management System is an Object-Oriented Programming (OOP) implementation in Python that models the various roles within a school, including students, teachers, and staff. It demonstrates key OOP principles such as inheritance, encapsulation, polymorphism, and method overriding, allowing for efficient handling of different entities and their specific functionalities.

## Features

- **Inheritance**: A base class `Person` with derived classes `Student`, `Teacher`, and `Staff`.
- **Encapsulation**: Secure handling of sensitive data like SSNs using getter and setter methods.
- **Polymorphism**: Unified handling of different entities through a common interface.
- **Method Overriding**: Specific duties defined for students, teachers, and staff.
- **Grade Assignment**: Students can receive grades and calculate their average.
- **Attendance Tracking**: Logs student attendance per class.
- **Teacher Class Management**: Teachers manage class schedules and subjects.
- **Staff Salary Calculation**: Staff salary computation based on various factors.

## Class Structure

### `Person` (Base Class)

Attributes:

- `name` (string)
- `age` (int)
- `address` (string)
- `_ssn` (string, encapsulated)

Methods:

- `get_ssn()`, `set_ssn()` - Encapsulation of SSN.
- `role_duties()` - General responsibilities (Overridden in subclasses).

### `Student` (Derived from `Person`)

Additional Attributes:

- `grades` (dict)
- `attendance_record` (dict)

Methods:

- `assign_grades(grades: dict)` - Assigns grades and calculates the average.
- `attendance(subject: str, present: bool)` - Marks attendance and tracks it.
- `role_duties()` - Overrides base method to define student responsibilities.

### `Teacher` (Derived from `Person`)

Additional Attributes:

- `subject` (string)
- `class_schedule` (dict)

Methods:

- `schedule_classes(schedule: dict)` - Assigns a class schedule.
- `role_duties()` - Overrides base method to define teacher responsibilities.

### `Staff` (Derived from `Person`)

Additional Attributes:

- `salary` (float)
- `years_of_service` (int)

Methods:

- `calculate_salary()` - Computes salary based on role and experience.
- `get_salary()` - Returns the calculated salary.
- `role_duties()` - Overrides base method to define staff responsibilities.

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/lahirudatascience/school_management_system
   ```
2. Navigate to the project directory:
   ```bash
   cd school_management_system
   ```
3. Run the Python script:
   ```bash
   python main.py
   ```

## Conclusion

This School Management System effectively utilizes OOP principles to structure and manage different roles in a school setting. The implementation demonstrates inheritance, encapsulation, polymorphism, and method overriding to create a scalable and maintainable system.
