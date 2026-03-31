import re

names = input()
pattern = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", names)

print(" ".join(pattern))