# Write a pyhton program to rename the file to "remove_by_python.txt"
# Search in google os module to remove the file name in python
import os
oldName="renameFile.txt"
newName="rename_by_python.txt"
with open(oldName) as f:
    content=f.read()
with open(newName,'w') as f:
    f.write(content)
os.remove(oldName)