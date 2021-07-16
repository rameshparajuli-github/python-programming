# Write a program to find sum of first n natural number using while loop
nam =int(input("Enter the natural number:  "))
sum=0
while(nam>0):
    sum=sum+nam
    nam=nam-1
print(sum)