import re

msg = "this is Regular Expression (RegEx) version 19.13"
obj = re.search("[0123][0-3]",msg)
print(obj)

msg2 = "342 112 111 121"
obj2 = re.search("[0-1][0-1][0-1]",msg2)
print(obj2)

obj3 = re.search('[0-9][0-9]',"99 100")
print(obj3)


obj4 = re.search('[0-9][0-2]',"99 100")
print(obj4)   #10

msg3 = '13.21 14.2'
print(re.search('[0-9][0-9].[0-9][0-9]',msg3)) # <re.Match object; span=(0, 5), match='13.21'>

# . matches any character except new line character (\n)

msg4 = 'this is 2026'
obj5 = re.search('[0-9].[0-9][0-9]',msg4)
print(obj5)

msg5 = '12.2'
print(re.search('[0-9][0-9][.][0-9]',msg5))