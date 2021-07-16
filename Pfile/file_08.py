# Write a program to mine a log file and find out whether it contains 'python'
with open('logFile.txt') as f:
    file= f.read()
    if 'python' in file.lower():
        print("Python is present in log  file")
    else:
        print("Python is not present in log file")
    
