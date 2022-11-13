#Write a Python program to remove the nth index character from a nonempty string.
str=input("Enter a string:: ")
n =int(input("Enter a Index Number:: "))
new_str= str[:n-1]+str[n:]
print(str[:n-1])
print(str[n:])
print(new_str)