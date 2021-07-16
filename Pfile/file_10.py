# Write a program to generate a multiplication table from 2 to 20 and it to the different file
# import os
for i in range(2, 21):
    with open(f"multiplication_table _of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j} = {i*j}\n")
            