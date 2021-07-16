

class Employee:
    company="Google"
Ramesh=Employee()
Ram=Employee()
print(Ramesh.company)
print(Ram.company)
Employee.company="YouTube"    #Changing the class attribute    
print(Ramesh.company)
print(Ram.company)

