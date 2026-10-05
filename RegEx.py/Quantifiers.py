import re
s1 ="The current Python is a programming language. python3.13"

# pat = r"[a-z][a-z][a-z]"
pat = r"[a-z]{3}"
# print(re.search(pat,s1))

pat1 = r"[A-z][a-z]{5}"   # only [a-z] mult by 5 not [A-z]

# print(re.search(pat1,s1))



pat2 = r"[A-z][a-z]{2,5}"   # only [a-z] mult by 5 not [A-z]

print(re.search(pat2,s1))

pat2 = r"[A-z][a-z]{2,5}" 
print(re.search(pat2,s1))