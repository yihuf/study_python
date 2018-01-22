'''
str.partition(sep)
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator,
the separator itself, and the part after the separator.
If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
'''
'''通过sep分隔字符串'''
print('ab:cd'.partition(':'))
str = 'hello world'.partition(' ')
for value in str:
    print(value)
