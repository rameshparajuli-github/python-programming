class Employee:
    def __init__(self):
        print("Initilizing the Employee")

    def getIncome(self):
        print(f"My income is 20000")


class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Initilizing the Programmer")

    def getAge(self):
        print("I am 20 years old")

# e=Employee()
p=Programmer()
