a=input("Enter the first number: ")
b=input("Enter the second number: ")
c=input("Enter the third number: ")

num1=int(a)
num2=int(b)
num3=int(c)

if(num1>num2 and num1>num3):
     print("First number is greater")
elif (num2>num1 and num2>num3):
     print("Second number is greater")
elif (num3>num1 and num3>num2):
     print("Third number is greater")

else:
    print("Error you enter the number")

