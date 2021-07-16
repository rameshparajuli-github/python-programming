class Employee:
    company="Google"
    def getSalary(self):    #Self parameter is automatically pass 
        print(f"Salary of employee working in {self.company} is {self.salary}")
Ramesh=Employee()
Ramesh.salary=10000
Ramesh.getSalary() # Employee.getSalary(Ramesh)
