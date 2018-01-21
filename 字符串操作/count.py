'''str.count(sub[, start[, end]]) '''
'''Return the number of non-overlapping occurrences of substring sub in the range [start, end].
 Optional arguments start and end are interpreted as in slice notation.'''
'''统计子字符串个数，查找范围为闭开区间，包括start但是不包括end'''
num1 = 'sssabcabcabcSSS'.count('abc')
print('num1 is {}'.format(num1))
num2 = 'sssabcabcabcSSS'.count('abc',5)
print('num2 is {}'.format(num2))
num3 = 'sssabcabcabcSSS'.count('abc',0,9)
print('num3 is {}'.format(num3))
