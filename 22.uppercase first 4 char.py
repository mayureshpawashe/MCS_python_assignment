#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase
# characters in the first 4 characters
def to_upper(str):
    counter = 0
    for i in str[:4]:
        if i.isupper():
            counter =counter + 1
    if counter > 1:
        return str.upper()
    else:
        return str

str = input("Enter the String:: ")
print(to_upper(str))