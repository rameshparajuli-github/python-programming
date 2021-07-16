'''Create a class with a class attribute a ;create an object from it and set a directly using object.a=o.
Does this change the class attribute  '''
class name:
    a="Ramesh"
obj=name()
obj.a="Ram"
print(name.a)
print(obj.a)