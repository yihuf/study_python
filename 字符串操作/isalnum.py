'''
str.isalnum()
Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
A character c is alphanumeric if one of the following returns True: c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric().
'''
'''判断所有字符是否都是文字或者数字'''
print('123'.isalnum())
print('12aA'.isalnum())
print('你好'.isalnum())
print('12+'.isalnum())
