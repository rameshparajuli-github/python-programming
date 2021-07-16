class Employee:     #parent class
    company = "Google"
    eCode = 6066


class Freelencer:     #parent class
    company = "Softteach"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelencer):     #child class
    name = "Ramesh"


p = Programmer()
p.upgradeLevel()
print(p.level)
