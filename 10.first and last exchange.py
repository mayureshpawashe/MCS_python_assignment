#Write a Python program to change a given string to a new string where the first and last chars have
# been exchanged.
str=input("Enter a String::")
new_string = str[-1]+str[1:-1]+str[0]
print(new_string)