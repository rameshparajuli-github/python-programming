'''Write a program to input name, marks and phone number of a students and 
format it using the format functon like below:'''

name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
phone=int(input("Enter your phone number: "))

detail="The name of the student is {},his marks are {},and phone number is {}."
output=detail.format(name, marks, phone)
print(output)