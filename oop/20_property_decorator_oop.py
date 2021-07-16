class Eymployee:
    company="Nepal Electricity"
    salary=50000
    salarybonus=5000


    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

# for set the property we use setter 
    @totalSalary.setter    #for change the total salary we use setter 
    def totalSalary(self,val):
        self.salarybonus= val - self.salary



e=Eymployee()
print(e.totalSalary)
e.totalSalary=500
print(e.salary)
print(e.salarybonus)