try:
    user = int(input("Enter a number: "))
    a = 1/user
    print(a)

except ValueError as e:   #  value error laii handel garcha jasto ko number mageko thau ma user le letter in inputgaryo vane value error aauncha teo error laii handel gaecha code crash huna denna 
    print("Please Enter a valid number")

except ZeroDivisionError as e: #Zero division error lai handel garcha 1/0 garyo vane error falcha taslai handel garcha 
    print("Make sure your are not dividing by Zero(0)")
print("Thanks Youu!")

