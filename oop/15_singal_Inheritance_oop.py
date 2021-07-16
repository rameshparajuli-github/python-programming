class Employee:  # ----> Base class
    company = "Google"

    def getDetail(self):
        print("I am a programmer ")


class Programmer(Employee):  # -----> Derived or child class
    language = "Python"
    company = "YouTube"

    def getDetail(self):
        print(f"The language is {self.language}")

    def getInfo(self):
        print("I am a python programmer ")


e = Employee()
e.getDetail()
p = Programmer()
p.getDetail()
