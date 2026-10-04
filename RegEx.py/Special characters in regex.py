import re
s1 ="Python is a programming language. python3.13"
# [A-Z],[a-z]

#pat =r"old/new"
#print(pat)
pat = r"[a-z][a-z]"
obj = re.search(pat,s1)
# print(obj)

# \d and \D
# \d matches 1 digit character. It is similar to [0-9]

pat1 = r"[a-z][a-z]\d"
obj1 = re.search(pat1,s1)
#print(obj1) # <re.Match object; span=(38, 41), match='on3'>

# \D matches 1 non-digit character. It is similar to [0-9]

pat2 = r"[a-z][a-z]\D"
obj2 = re.search(pat2,s1)
#print(obj2)     # <re.Match object; span=(1, 4), match='yth'>

# \s , \S
# \s ==> any whitespace character tab and new line char
s2 ="Python### is a programming language. python3.13"
pat3 = r"[a-z][a-z]\s"
obj3 = re.search(pat3,s2)
#print(obj3) 

# \S ==> opposite of \s. matches any char except space, \n and \t

s3 = """
Hello , this regex in phython 
from re module
bye ! !!! 
"""

pat4 =r"[a-z][a-z][a-z][a-z]\S"
obj4 = re.search(pat4,s3)
print(obj4)