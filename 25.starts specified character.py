#Write a Python program to check whether a string starts with specified characters.
str=input("Enter a string:: ")
char=input("Enter Specified character:: ")
if str.startswith(char):  #here we use startwith method
    print("Yes it starts")
else:
    print("Not Start")