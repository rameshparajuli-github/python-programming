'''A file contains a word "ramesh" multiple times. You need to write a program Which replace this word 
with ###### by updating the same file.'''
with open('poem.txt') as f:
    data = f.read()
data= data.replace("ramesh","$%^$#@^#")
with open("poem.txt",'w') as f:
    data= f.write(data)
