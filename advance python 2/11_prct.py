'''Write a program to find the maximum of the number in a list using the reduce function'''

from functools import reduce
ls = [2,3,4,5,9]
a=reduce(max,ls)
print(a)