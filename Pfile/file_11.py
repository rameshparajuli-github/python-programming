# import os
def game():
    return 201
score = game()
with open('highscoor.txt') as f:
    highscoor = f.read()
if highscoor=='':
    with open('highscoor.txt','w') as f:
        f.write(str(score))

elif int(highscoor)<score:
    with open('highscoor.txt','w') as f:
        f.write(str(score))