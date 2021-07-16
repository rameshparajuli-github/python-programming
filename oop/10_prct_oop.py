'''Creat a class programmer for storing information of few programmers working at microsoft '''


class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Creating information ")

    def getInfo(self):
        print(
            f"The name of the{self.company}  programmer  is {self.name}")
        print(
            f"The salary of the {self.company} programmer  is {self.salary}")
        print(
            f"The subunit of the {self.company} programmer is {self.subunit}")


ramesh = Programmer("Ramesh", 100000, "Google")
ramesh.getInfo()
