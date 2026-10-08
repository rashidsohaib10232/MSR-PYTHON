import re

phones = "Sohaib - 7860003623, Ateeb-9898123489, Khalid-8912398958"

pat = r"\d{10}"

match = re.findall(pat,phones)
print(match)  
print(pat)