import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(response.status_code) # returns 200! Okay!

print(response)