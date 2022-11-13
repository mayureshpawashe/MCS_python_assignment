#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string
#length is less than 2, return instead of the empty string. Sample String : ‘Learning Python’ Expected Result
#: ‘Leon’ Sample String : 'Pi' Expected Result : 'PiPi' Sample String : ' S' Expected Result : Empty String
str1=str(input("Enter String::"))
if len(str1) > 1:
    print(str1[:2]+str1[-2:])
else:
    print('empty string')