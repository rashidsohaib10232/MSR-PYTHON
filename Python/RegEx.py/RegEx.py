import re

msg = "this is Regular Expression (RegEx) "

# print("this" in msg)

# print("Is" in msg)

x = re.search("R5e",msg)
# print(x)

if x:
    print("found")
else:
    print("Not found")