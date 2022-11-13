#Write a Python function to create the HTML string with tags around the word(s). Sample function and
#result : add_tags('i', 'Python 3.7') -> '<i>Python 3.7</i>' add_tags('b', 'Python 3.7 Tutorial') ->
# '<b>Python 3.7 Tutorial </b>'
def add_tags(tag,text):
    return "<"+tag+">"+text+"<"+tag+">"

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))