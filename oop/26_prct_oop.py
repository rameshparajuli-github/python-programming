'''Create a class Employee and salary ans increment properties to it
Write a method salaryAfterIncrement method with a @property decorator 
with a setter which changes the value of increment based on the salary.'''



class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaeyAfterIncome(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.salaeyAfterIncome)
print(e.increment)
e.salaeyAfterIncome=2000
print(e.increment)
