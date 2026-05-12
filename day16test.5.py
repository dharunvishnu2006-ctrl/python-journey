class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.__salary = salary  
   
    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be above 0")

    def describe(self):
        return f"{self.name} works in {self.department} dept"

class Manager(Employee):
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size

    def manager_info(self):
        return f"Manages {self.team_size} people"

    def describe(self):
        return f"{self.name} is a Manager in {self.department}"


emp = Employee("Ravi", "HR", 50000)
print(emp.describe())
print(emp.get_salary())

mgr = Manager("Dharun", "IT", 80000, 10)
print(mgr.describe())
print(mgr.manager_info())