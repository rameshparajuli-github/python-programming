''' Write a program to read a text from a given file 'poem.txt'
and find out wheather it contains the word twinkle.'''
import os 
f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present in text")
else:
    print("Twinkle is not present in text")
f.close()