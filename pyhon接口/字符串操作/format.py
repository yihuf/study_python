'''str.format(*args, **kwargs)
Perform a string formatting operation.
The string on which this method is called can contain literal text or replacement fields delimited by braces {}.
Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument.
Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
'''
'''可以格式化字符串，类似于sprintf'''
print('sss{}{}SSS'.format('ac','ad'))
print('sss{0}{1}SSS'.format('ac',1))
print('sss{a}{b}SSS'.format(a=2,b='cc'))
