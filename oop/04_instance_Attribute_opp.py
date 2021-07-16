
class Employee:
    company="Google"
Ramesh=Employee()
Ram=Employee()
print(Ramesh.company)
print(Ram.company)
Employee.company="YouTube"    #Changing the class attribute    
print(Ramesh.company)
print(Ram.company)

# instance attribute 
Ramesh.salary=5000
Ram.salary=4000
print(Ramesh.salary)
print(Ram.salary)
