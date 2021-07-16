# This is the letter by take the keywords from users..
letter = ''' Dear <|NAME|>
Congratulation your are selected to our company 
Your are selected!
Have a great day ahead!
Thank you for register your name!

Date: <|DATE|>'''
name = input("Enter your Name: ")
date = input("Enter Date: ")
letter= letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE|>",date)

print(letter)
