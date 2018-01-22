'''
str.istitle()
Return true if the string is a titlecased string and there is at least one character,
for example uppercase characters may only follow uncased characters and lowercase characters only cased ones.
Return false otherwise.
'''
'''字符串的单词的首字母(出现的第一个字母)大写，其余字母小写'''

print('Hello World'.istitle())
print('HEllo World'.istitle())
print('hello World'.istitle())
print('Hello 1 World'.istitle())
print('Hello W1orld'.istitle())
print('Hello World'.istitle())
print('Hello 1world'.istitle())
