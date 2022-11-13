#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'
str=input("Enter String ::")
if len(str)<3:
    new_str=str
elif str[-3:]=='ing':
    new_str=str+'ly'
else:
    new_str=str+'ing'
print (new_str)