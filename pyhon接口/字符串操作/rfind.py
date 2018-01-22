'''
str.rfind(sub[, start[, end]])
Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end].
Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
'''
'''从右边开始查找sub'''

print('abcdef'.find('a'))
print('abcdef'.rfind('a'))

print('abcdefa'.find('a'))
print('abcdefa'.rfind('a'))
