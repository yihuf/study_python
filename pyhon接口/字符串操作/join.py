'''
str.join(iterable)
Return a string which is the concatenation of the strings in iterable.
 A TypeError will be raised if there are any non-string values in iterable,
  including bytes objects. The separator between elements is the string providing this method.
'''
'''如果iterable是元组或者列表，则将str作为分隔符分隔里面的元素，如果iterable是字符串，则分隔每个字符'''
'''如果iterable是字典，则分隔key值，如果含有非字符串，则报错'''
str = '/'
print(str.join('ssss'))
print(str.join(('ssss','aaaa','123'))) #元组
print(str.join(['ssss','aaaa','123'])) #列表
print(str.join({'a':'b','c':'d'}))
print(str.join(['ssss']))
print(str.join(['ssss',123]))

