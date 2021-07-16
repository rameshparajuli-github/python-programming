import random
def gameWin(comp,you):
    # If two values are equal , declear tie
    if comp == you:
        return None

    # Check for all possibilities when computer chooase s
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
  # Check for all possibilities when computer chooase p
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
  # Check for all possibilities when computer chooase r
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

print("Comp Turn: Rock(r) , Paper(p) or Scissor(s):  ")
randomNO=random.randint(1,3)
if randomNO == 1:
    comp='r'
elif randomNO == 2:
    comp='p'
elif randomNO == 3:
    comp='s'

you= input("Your Turn: Rock(r) Paper(p) or Sisscor(s)?:  ")
a=gameWin(comp,you)
print(f"Computer choose {comp} ")
print(f"You choose {you} ")
if a == None:
    print("The game is tie")
elif a:
    print("You Win ")
else:
    print("You lose")