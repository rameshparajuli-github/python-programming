'''A list contains the multiplication table of 7 . 
write a program to convert  it to a vertical string of same number'''

ls = [str(i*7) for i in range(1,11)]
print(ls)
VarticalTable="\n".join(ls)
print(VarticalTable)