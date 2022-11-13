#Check if given string is palindrome
str1=str(input("Enter String to Check::"))
#str2=str1[: :-1]
if(str1==str1[::-1]):
    print("String is Palindrome")
else:
    print("String is not Palimdrome")