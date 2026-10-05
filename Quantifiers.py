import re
s1 ="Python is a programming language. python3.13"

# pat = r"[a-z][a-z][a-z]"
pat = r"[a-z]{3}"
print(re.search(pat,s1))

print("h")