a=54   # Global Variable
def func1():
    global a     # This line change Global variable 
    print(f"This statement:{a}")
    a=9   #  Local Variable  # yadi teo mathi ko global a use nagareko vaya yo line ma 54 naii print hunthyo 
    print(f"This statement:{a}")
func1()
print(f"This statement:{a}")
