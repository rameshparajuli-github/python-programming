# Write a program to fins out wheather a file is identical and  matches the content of a file using python
files1='poem.txt'
files2='copy.txt'

with open(files1) as f:
    f1=f.read()
    
with open(files2) as f:
    f2=f.read()
if f1==f2:
    print("This is identical file ")
else:
    print("This is not identical file")
