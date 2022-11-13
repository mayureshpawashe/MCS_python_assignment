#Write a Python program to remove the characters which have odd index values of a given string.
str=input("Enter a string::")
new_string = ''
for i in range(len(str)):
    if i%2 == 0:
        new_string =new_string + str[i]
print(new_string)