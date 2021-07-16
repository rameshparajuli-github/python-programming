# Write a program to make a copy of a text file 'copy.txt'
with open('meaning.txt') as f:
    meaning =f.read()

with open("copy.txt",'w') as f:
    f.write(meaning)