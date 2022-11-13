#Write a Python function to reverses a string if it's length is a multiple of 4.
def rev_str(str):
    if len(str)%4 == 0:
        my_list = str[::-1]
        return ''.join(my_list)
    else:
        return str

str= input("Enter the String:: ")
print(rev_str(str))