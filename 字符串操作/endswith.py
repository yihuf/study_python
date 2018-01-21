'''
str.endswith(suffix[, start[, end]])
Return True if the string ends with the specified suffix, otherwise return False.
suffix can also be a tuple of suffixes to look for.
With optional start, test beginning at that position.
With optional end, stop comparing at that position.
'''
'''判断目标字符串是否以指定后缀结尾，后缀也可以是一个元组里面的某个字符串'''
ret = 'sssSSS'.endswith(('SS','as','bS'))
print(ret)
ret = 'sssSSS'.endswith(('as','bS'))
print(ret)
