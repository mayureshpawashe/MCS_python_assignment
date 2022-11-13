#Write a Python program to swap comma and dot in a string.
str1=input("Enter a String::")
print(str1)
swap = str.maketrans(',.', '.,')
str2 = str1.translate(swap)
print(str2)