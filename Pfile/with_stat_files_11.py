# With statement in file 
with open('main.txt','r') as f:
    a=f.read()
print(a)
#No need to close the file in with statement f.close