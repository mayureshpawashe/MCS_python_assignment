#Write a Python program to get the last part of a string before a specified character.
def get_last_part(str, char):
    pos=str.rfind(char)
    return str[:pos]

print(get_last_part('India is-my-Country', "-"))