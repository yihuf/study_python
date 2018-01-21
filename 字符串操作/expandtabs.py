'''
str.expandtabs(tabsize=8)
Return a copy of the string where all tab characters are replaced by one or more spaces,
depending on the current column and the given tab size.
Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on).
To expand the string, the current column is set to zero and the string is examined character by character.
If the character is a tab (\t), one or more space characters are inserted in the result
 until the current column is equal to the next tab position. (The tab character itself is not copied.)
If the character is a newline (\n) or return (\r), it is copied and the current column is reset to zero.
Any other character is copied unchanged and the current column is incremented by one regardless of how
 the character is represented when printed.
'''
'''把tab替换为空格，一个tab默认替换为8个空格'''
'''从左到右依次替换tab'''
'''如果tab左侧有其它字符（非tab字符），则填充空格数为tabsize减去其它字符的长度'''
'''如果填充空格数小于等于0，则将tabsize加一次后再重复上面的步骤，直到不满足此条'''
'''tabsize = num'''
'''tabsize = tabsize + num'''
'''
>>> '01\t012\t0123\t01234'.expandtabs()
'01      012     0123    01234'
>>> '01\t012\t0123\t01234'.expandtabs(4)
'01  012 0123    01234'
'''
str = 'sss\t\tSSSS'
size1 = len(str)
print(str,end=' ')
print('before expandtabs size {}'.format(size1))
str1 = str.expandtabs(4)
print(str1,end=' ')
size2 = len(str1)
print('after expandtabs size {}'.format(size2))
