#Write a Python program to strip a set of characters from a string.
my_string = input("Enter String:: ")
my_list = [x for x in my_string if x not in 'mayur']
print(''.join(my_list))