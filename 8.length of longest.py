#Write a Python function that takes a list of words and returns the length of the longest one.
words=input("Enter a few word of String:: ")
list=words.split() #the split function convert str to list

max=0
for str in list:
    if len(str)>max:
        max=len(str)

print(str)
print(max)