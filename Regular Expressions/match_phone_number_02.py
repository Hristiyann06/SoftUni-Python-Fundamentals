import re

phone_numbers = input()

pattern = re.findall(r"\+359(?:[ -])2(?:[ -])\d{3}(?:[ -])\d{4}\b", phone_numbers)

print(", ".join(pattern))