# Write the program to find the greatest of four number enter by the user
num1= int(input("Enter the number1: "))
num2= int(input("Enter the number2: "))
num3= int(input("Enter the number3: "))
num4= int(input("Enter the number4: "))
if (num1>num4):
    f1= num1
else:
    f1= num4
if (num2>num3):
    f2= num2
else:
    f2= num3
if(f1>f2):
    print(str(f1) + " is greater ")
if(f2>f1):
    print(str(f2) + " is greater ")
