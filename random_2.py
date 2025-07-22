# removing all leading white spaces
def removeAllLeadingWhiteSpaces(str):
    return str.lstrip()
a=removeAllLeadingWhiteSpaces("   aaa    ")
print("output1...:",a)

# replace all occurance in the string
def replaceAllOccurance(str,replace_word,replace_ele):
    return str.replace(replace_word,replace_ele)
b=replaceAllOccurance("hello world, world is great","world","python")
print("output2...",b)