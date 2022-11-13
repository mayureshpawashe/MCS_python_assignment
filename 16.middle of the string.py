#Write a Python function to insert a string in the middle of a string. Sample function and result
#: insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] insert_sting_middle('{{}}', 'Jython') -> {{Jython}}
def insert(main_str,middle_str):
    main_len=len(main_str)
    middle=int(main_len/2)
    return main_str[:middle] + middle_str + main_str[middle:]

print(insert('[[]]','Python'))
print(insert('{{}}','PHP'))
print(insert('<<>>','HTML'))