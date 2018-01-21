'''
str.index(sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found.
'''
'''index操作在找不到目标的情况下会直接出错'''
result1 = 'sssSSS'.find('aa')
print(result1)

result2 = 'sssSSS'.index('SS')
print(result2)

result = 'sssSSS'.index('aa')
print(result)


