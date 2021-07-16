# Write a python function to remove a given words from a string and strip it at the same time
def remove_and_strip(string,word):
    newStri=string.replace(word,"")
    return newStri.strip() #space remove garcha 


a="     My name is ramesh parajuli      "
b=remove_and_strip(a,"My")
print(b)