
from datetime import datetime

class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=0):
        self.name = name
        
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")      
        else:
            self.salary = salary
    
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")  
        
        elif self.salary + amount <  Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")
      
        else: 
            self.salary += amount
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
    
    def give_raise(self, amount):
        self.salary = self.salary + amount
    
    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        r = "Employee(\"{name}\", {salary})".format(name=self.name,
         salary=self.salary)  
        return r
        
# define a child class Manager and add a display method 
# that prints the name
class Manager(Employee):
  def display(self):
    print("Manager {}".format(self.name))

  def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

  # Add a give_raise method (example of polymorphism)
  def give_raise(self, amount, bonus=1.05):
      Employee.give_raise(self, amount*bonus)
    
    


      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()

mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)
print(mngr)
print(repr(mngr))