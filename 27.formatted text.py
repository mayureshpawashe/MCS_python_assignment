#Write a Python program to display formatted text (width=50) as output
import textwrap

sample_text = 'hii iam dark'
print()
print(textwrap.fill(sample_text, width=50))
print()