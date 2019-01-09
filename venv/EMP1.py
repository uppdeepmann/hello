
from EMP import Employee

class Employee_new(Employee):

      def __init__(self, name, salary,age):
         Employee.__init__(self, name, salary)
         self.age = age


      def displayEmployee(self):
          print("Name : ", self.name, ", Pay: ", self.salary)

      def display_age(self):
          print ("Age: ", self.age )
