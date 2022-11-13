#Write a Python program to count repeated characters in a string.
str=input("Enter a string:: ")
dict={}
for letter in str:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1
for key,value in dict.items():
    print(key,value)