# ^ => caret
import re
s1 = "Python is a programming language"

pat = r"[a-z]{8}"

print(re.search(pat,s1))

print(re.search((r"^[a-z]{8}"),s1))

# $ => matches the end of the string
print(re.search(r'[a-z]{8}$',s1))