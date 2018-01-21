'''str.center(width[, fillchar]) '''
'''Return centered in a string of length width.
Padding is done using the specified fillchar (default is an ASCII space).
The original string is returned if width is less than or equal to len(s). '''
'''使目标字符串被填充字符置为输出字符串中间'''
str = 'sssSSS'.center(13,'a')
print(str)
