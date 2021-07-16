# Number guessing game
import random
randNumber = random.randint(1, 100)
# print(randNumber)   # yo line le random number laii pane show garcha
userGuess = None  # userGuess chaii hamle define garnu parcha
guesses = 0

# jaba samma user le enter gareko number random number samma equal hunna taba samma input mageko magaii garcha
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess number: "))
    guesses += 1  # kati chotti guessed garyo
    if(userGuess == randNumber):  # yadi equal vayo vane loop exit huncha
        print("You guessed the right number ")
    else:
        if(userGuess > randNumber):
            print("You guessed worng number!Enter the small number")
        else:
            print("You guessed worng number!Enter the larger number")
print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    highscore=int(f.read())
if(guesses<highscore):
    print("You broke the high score")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))

        
    

