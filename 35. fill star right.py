#Write a Python program to print the following integers with '*' on the right of specified width.
my_string = input("Enter an integer:: ")

print('{:*<5s}'.format(my_string))