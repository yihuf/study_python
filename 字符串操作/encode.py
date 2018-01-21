'''str.encode(encoding="utf-8", errors="strict") '''
'''Return an encoded version of the string as a bytes object.
Default encoding is 'utf-8'.
errors may be given to set a different error handling scheme.
The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any
other name registered via codecs.register_error(), see section Error Handlers.
For a list of possible encodings, see section Standard Encodings.'''

str = 'sssSSS'.encode()
print(str)
