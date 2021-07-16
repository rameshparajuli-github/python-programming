# Write a program to find out the line number where pyhton is present from question no.6
file =True
i=1
with open('logFile.txt') as f:
    while file:
        file= f.readline()
        if 'python' in file.lower():
            print(file)
            print(f"Python is present in log  file {i}")
        i+=1