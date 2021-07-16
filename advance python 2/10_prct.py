'''Write a program to filter a list of numbers which are divisible by 5'''
from typing import List


# def divisible(num):
#     if num % 5 ==0:
#         return True
#     else:
#         return False
ls = [1,3,5,10,15,9,8,25,55,50,33,29,78]
# print(list(filter(divisible ,ls)))





# By using lambda function
num= filter(lambda num: num % 5 == 0 ,ls)
print(list(num))


    
    