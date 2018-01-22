'''
str.isspace()
Return true if there are only whitespace characters in the string and there is at least one character, false otherwise.
'''
'''判断字符是否全是空格（space）,，包括tab字符（\t）'''

print('\t')
print('\t'.isspace())
print(len('\t'.expandtabs()))
print(' ')
print(' '.isspace())
