'''
str.isdigit()
Return true if all characters in the string are digits and there is at least one character, false otherwise.
Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits.
'''
'''和isdecimal类似，但是isdigit可以识别特殊格式的数字，比如例子中的兼容上标数字'''
print('1234⁴⁵⁶⁷⁸⁹'.isdigit())
print('1234⁴⁵⁶⁷⁸⁹'.isdecimal())
