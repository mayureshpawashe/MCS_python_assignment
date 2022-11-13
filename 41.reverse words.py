#Write a Python program to reverse words in a string.
sentence=input("Enter a sentence ::")

my_list=sentence.split()
print(' '.join(my_list[::-1]))