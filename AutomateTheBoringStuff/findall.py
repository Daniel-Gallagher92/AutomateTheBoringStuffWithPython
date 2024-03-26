import re #whenever you anticipate working with regular expressions, just import immediately 

phoneRegex = re.compile(r'\(\d{3}\) \d{3}-\d{4}')

clientNumbers = '''David R (795) 652-7267,
Sallie M (525) 911-1695,
Robert D (659) 981-5076,
Jake R (276) 553-0269,
Brock M (428) 935-7371,
Shelby M (832) 216-8733,
Francis F (347) 537-0690,
Shaggy D (301) 353-4748'''

matchedNumbers = phoneRegex.findall(clientNumbers)

print(matchedNumbers)