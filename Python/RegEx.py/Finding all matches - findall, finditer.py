import re

# match()

s1 = "We are learning regex in Pyhton"
pat = r"[a-z]{3}"
print(re.search(pat,s1))

phone = "MSR - 9455593777, rock - 999999999999999999999999999939999,  NSR - 8939095438 , mark - 1239084567 , python3.13.5"
pat = r"[0-9]{10}"

print(re.search(r"[0-9]{10}",phone))


#print(len('8939095438'))

# findall
print(re.findall(r"[0-9]{10}",phone))

print(re.findall(r"[0-9]+",phone))  # i get all the no.

# fethc all phone numbers the phone numbers are exactly 7 digit and should not eceed 15 digit

print(re.findall(r"[0-9]{7,15}",phone))

# fethc all phone numbers the phone numbers are atleat 7 digit
print(re.findall(r"[0-9]{7,}",phone)) # 7 or more

# \b
# fetch all phone no. the phone no. are exactly 7 digits and should not exced 15 digit

print(re.findall(r"\b[0-9]{7,15}\b",phone)) 


# finditer()

print(re.finditer(r"[0-9]{7,15}",phone)) 

mathces = re.finditer(r"[0-9]{7,15}",phone)

for i in mathces:
    print(i)


