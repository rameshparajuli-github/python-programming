ls = [1, 2, 6, 8, 9, 10, 4, 90, 88, 778, 3, 7, 5]
# b=[]
# for item in ls:
#     if item%2==0:
#         b.append(item)
# print(b)


# list comprehensions(Shortcut )
b = [item for item in ls if item % 2 == 0]
print(b)
