#Write a Python program to count the occurrences of each word in a given sentence.
str=input("Enter String of words:: ")
list=str.split()
dict = {}
for word in list:
    if word in dict:
        dict[word]=dict[word] + 1
    else:
        dict[word] = 1
print(dict)