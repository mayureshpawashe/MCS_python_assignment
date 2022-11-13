#Write a Python program to lowercase first n characters in a string
str=input('Enter a string::')
n = int(input("Enter Value of n::"))
print(str[:n].lower()+str[n:])
