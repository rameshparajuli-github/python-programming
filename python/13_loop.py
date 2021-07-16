# Write a program to find a factorial of given number
# Some Example
# n!=1 X 2 X 3 X 4 X......n
# 5!=1 X 2 X 3 X 4
a =int(input("Enter the number: "))
factorial = 1
for i in range(1, a+1):
    factorial = factorial * i
print(f"The factorial of {a} is {factorial}")