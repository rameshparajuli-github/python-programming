letter ='''Dear friend <|NAME|>
congratulation!

Thank you!
Date: <|DATE|>'''
name =input("Enter your Name: ")
date =input("Enter your date: ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)


