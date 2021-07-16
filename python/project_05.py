
text= input("Enter the text: \n")

if ("make money" in text):
    spam= True
elif ("buy now" in text):
    spam= True
elif ("click this" in text):
    spam= True
elif ("suscribe this" in text):
    spam= True
else:
    spam= False


if(spam):
    print("This Text  is spam ")
else:
    print("This Text is not  spam ")