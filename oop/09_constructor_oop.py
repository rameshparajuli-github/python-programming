class Employee:
    company="Google"
    
    # self pass itself but we have to pass name, salary like that 
    def __init__(self,name ,salary, subunit): #init run automatically
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Creating Employee")
    def getDetail(self):  #  method 
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

Ramesh=Employee("Ramesh",100000,"Google") # We pass the name, salary , subunit 
Ramesh.getDetail()


   