import array as arr
values=arr.array('i',[])
n=int(input("Enter the length of array: "))

for i in range(n):
    x=int(input(f"Enter the {i+1} value: "))
    values.append(x)
    
for i in range(n):
    print(values[i])