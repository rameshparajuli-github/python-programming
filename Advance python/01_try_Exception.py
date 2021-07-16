while(True):
    print("If you want to quit this game please press q")
    user = input("Enter a number:  ")
    if(user == "q"):
        break
    try:
        user = int(user)
        if(user > 9):
            print("You Enter the number greater then nine (9)")
    except Exception as e:  #yo line le erro lai handel garcha matlab ke Error faldaina ,,,code crash hudaina 
        print(f"Your input resulted is an error: {e}")
print("Thank for playgame ")
