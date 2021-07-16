'''Write a list comprehension to print a list which contains the multiplication table of a user entered number'''

num=int(input("Enter the number: "))
table=[num*i for i in range(1,11)]
print(table)