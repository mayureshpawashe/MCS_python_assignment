#Write a Python program to check if a string contains all letters of the alphabet.
str= input("Enter a string:: ")
alphabet='abcdefghijklmnopqrstuvwxyz'
counter=0
for letter in alphabet:
    if letter in str.lower():
        counter=counter+1
    else:
        break
if counter == 26:
    print('The String Contains all alphabet')
else:
    print('The String not Contain all Alphabet')
