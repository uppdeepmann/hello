from EMP import Employee

from EMP1 import Employee_new


emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)


emp1.displayEmployee()
emp2.displayEmployee()

# Inheritance

emp3 = Employee_new("Deep", 8000, 33)
emp3.displayEmployee()
emp3.display_age()

