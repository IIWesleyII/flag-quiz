import requests
iso_json = requests.get("https://flagcdn.com/en/codes.json").json()
print(iso_json)