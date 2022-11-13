#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return
#the resulting string. Sample String : 'The music is not that poor!' Expected Result : 'The music is good!'
str=input("Enter a string:: ")
not_pos=str.find('not') #return int value
poor_pos=str.find('poor') #return int value
if not_pos < poor_pos :
    new_string=str[:not_pos] + 'good'
else:
    new_string=str

print(new_string)