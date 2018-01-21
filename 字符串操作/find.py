'''
str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end].
 Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
'''
'''查找字符串，仅在需要返回索引时调用，否则使用in'''
print('sssSSS'.find('SS'))
print('SS' in 'sssSSS')
