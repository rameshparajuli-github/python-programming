'''Create a class pets from a class Animal and further create class Dog From Pets .
 Add a method bark to class dog '''


class Animal:
    animalType = "Mammal"


class Pets(Animal):
    color = "White"


class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow!")

a=Animal()
p=Pets()
d=Dog()
d.bark()
print(d.color)
print(p.animalType)