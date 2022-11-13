#Write a Python program to count and display the vowels of a given text.
n=input("Enter a string: ")
c=0
print("The vowels are: ")
for i in n:
 if i in "AEIOUaeiou":
     print(i)
     c=c+1

print("Total Number of Vowels is %d"%c)