'''
class Employee:
    name = "Ramesh"
    salary = 20000
    company = "Google"

    def changeSalary(self, sal):     #Class ko salary change hunna instance ko salary mattra change huncha 
        self.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(40000)      #Class Employee ko salary change hunna instance ma change huncha add garyo vane  
print(e.salary)
print(Employee.salary)

'''



#Alternative method  to change the class 
'''
class Employee:
    name = "Ramesh"
    salary = 20000
    company = "Google"

    def changeSalary(self, sal):     
        self.__class__.salary = sal   #Its change the class salary ----> __class__

e = Employee()
print(e.salary)
e.changeSalary(40000)     
print(e.salary)
print(Employee.salary)

'''




# We can use @classmethod decorator to change the class
class Employee:
    name = "Ramesh"
    salary = 20000
    company = "Google"

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal


e = Employee()
print(e.salary)
e.changeSalary(40000)     
print(e.salary)
print(Employee.salary)