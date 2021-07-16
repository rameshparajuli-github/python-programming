def square(num):
    return num*num


ls = [1, 2, 4]
# method 1
# ls2 = []
# for item in ls:
#     ls2.append(square(item))
# print(ls2)


# method 2 By using map 
print(list(map(square,ls)))