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


n1 = Number(5)
n2 = Number(7)
sum = n1 + n2
mul = n1 * n2

print(sum)
print(mul)
