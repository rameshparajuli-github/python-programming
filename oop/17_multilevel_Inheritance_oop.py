class Person:
    country = "Nepal"

    def getAge(self):
        print("I am 20 years old")


class Employee(Person):
    company = "Google"

    def getIncome(self):
        print(f"My income is 20000")


class Programmer(Employee):
    place = "Pokhara"

    def officeWork(self):
        super().officeWork()
        print("I have to go at 11 am")


p = Person()
e = Employee()
pr = Programmer()
print(p.country)
# print(p.place) #this line throw error
p.getAge()
pr.getIncome()
print(pr.company)
