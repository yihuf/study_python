'''Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.'''
'''和lower类似，但是支持其它语言转化为小写，3.3版本新增'''
str = "sssSSS".casefold()
print(str)
