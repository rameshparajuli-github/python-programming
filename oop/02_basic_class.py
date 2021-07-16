class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
ramesh=Employee('Ramesh','Parajuli',45000)
ram=Employee('Ram','Thapa',45000)

print(ram.fname,ramesh.fname)