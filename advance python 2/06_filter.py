def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10=lambda num: num<10 #lambda function also we can use in filter method

ls = [1, 24, 56, 10, 3, 4, 90, 55, 44, 33, 57]
print(list(filter(greater_than_5, ls)))
print(list(filter(g10, ls)))
