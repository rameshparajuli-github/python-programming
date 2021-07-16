class CitizenForm:
    formType="CitizenForm"
    def printData(self):
        print(f"Name is {self.name} ")
        print(f"Address is {self.address} ")
CitizenForm=CitizenForm()
CitizenForm.name="Ramesh Parajuli"
CitizenForm.address="pokhara"
CitizenForm.printData()