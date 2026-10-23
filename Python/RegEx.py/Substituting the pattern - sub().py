import re

# sub()

s1 = "Sunday, Monday, Tuesday, Monday, Sunday, Saturday"
# pat = "Sunday"
pat = r"S[a-z]+"
rep = "Friday"

# res = re.sub(pat, rep, s1, count=1)
res = re.sub(pat, rep, s1,)
print(res)

msg = "We are learning re. Re RE Re re has a pattern we can find pattern in the given string also we can search any thing fromm the string"

patt = r"\bre\b"
repp = "Regular Expression"
ress = re.sub(patt, repp, msg, flags=re.IGNORECASE)
print(ress)


phone_nums = "+91-1234123123, +91-9999999999"

patPhone = r"[+-]"
repPhone = ""

print(re.sub(patPhone, repPhone, phone_nums, flags=re.IGNORECASE))


