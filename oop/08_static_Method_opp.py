class Employee:
    company="Google"
    def getSalary(self, signature):
        print(f"The Salary of the {self.company} is {self.salary} \n{signature}")
    @staticmethod
    def greet():
        print("Hello Ramesh")
Ramesh=Employee()
Ramesh.salary=10000
Ramesh.getSalary("Thanks!")
Ramesh.greet()
   