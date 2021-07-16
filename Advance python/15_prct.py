'''Store the multiplication tables generated in problem 3 in a file named table.txt'''

num = int(input("Enter the number: "))
table = [num*i for i in range(1, 11)]
print(table)
with open("table.txt", "a") as f:
    f.write(str(table))
    f.write('\n')




