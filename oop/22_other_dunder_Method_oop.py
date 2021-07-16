# operator overloading 
class Number:
    def __init__(self, num) -> None:
        self.num = num
# for overloaded you have to use dunder method

    def __add__(self, num2):  # if you want overload the add you have to use __add__
        print("lets add")
        return self.num + num2.num

    def __mul__(self, num2):  # if you want overload the multiply you have to use __mul__
        print("lets multipy")
        return self.num * num2.num


    def __str__(self):
        return f"Decimal Number: {self.num}"
n= Number(9)
print(n)