#Write a Python program to get a string from a given string where all occurrences of its first char
#have been changed to '$', except the first char itself. Sample String : 'restart' Expected Result : 'resta$t'
str1=str(input("Enter The String::"))
new_str=str1[0]
for i in range(1, len(str1)):
    if str1[i] == str1[0]:
        new_str =new_str+'$'
    else:
        new_str =new_str + str1[i]
print(new_str)