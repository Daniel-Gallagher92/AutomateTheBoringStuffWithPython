message = "It was a bright, cold day in March two thousand and twenty four"

count = {}

for character in message.upper(): 
  count.setdefault(character, 0)
  count[character] = count[character] + 1
  
print(count)