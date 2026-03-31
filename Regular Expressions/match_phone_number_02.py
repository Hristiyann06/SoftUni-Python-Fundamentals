import re

phone_numbers = input()

pattern = re.findall(r"\+359([ -])2\1\d{3}\1\d{4}\b", phone_numbers)

print(" ".join(pattern))