#Write a Python program to display a number in left, right and center aligned of width 10.
my_num = float(input("enter a number "))

print('{:<10}'.format(my_num))
print('{:>10}'.format(my_num))
print('{:^10}'.format(my_num))