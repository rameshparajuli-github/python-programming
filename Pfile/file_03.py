# Replace  a program 4 for a list of such word to be consord
words =["parajuli","programmar"]
with open('poem.txt') as f:
    data = f.read()
    for word in words:
        data= data.replace(word,"$%^$#@^#")
with open("poem.txt",'w') as f:
    data= f.write(data)
