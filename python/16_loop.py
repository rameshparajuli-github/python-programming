# Write a multiplcation table by using for loop.
a= int(input("Enter the number you want multiply:  "))

b= int(input("Enter the number how many times do you want multiply:  "))
for b in range(1,b):
    print(str(a) + "X"  + str(b) +  "=" + str(a*b))
    # By using f string
    #  print(f"{a} X {b} = {a*b}")   
    # 

    # reverse multiply
# a= int(input("Enter the number you want multiply:  "))
# b= int(input("Enter the number how many times do you want multiply:  "))
# for b in range(b-1,0,-1):
#     print(str(a) + "X"  + str(b) +  "=" + str(a*b))  