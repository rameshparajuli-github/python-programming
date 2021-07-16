
class Employee:
    company="Google"
    def getSalary(self):    #Self parameter is automatically pass 
        print("Salary is 10000")
Ramesh=Employee()
Ramesh.getSalary() # Employee.getSalary(Ramesh)
