import re

# alice.cool_123@example.com

f = open('RegEx.py\StudentsMail.txt','r')
fech = f.read()
pat = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"

mat = re.finditer(pat,fech)
count =1
for i in mat:
    print(count,'.',i.group())
    count +=1
    

