import json

with open("LinkedInProfiles.json", "r", encoding="utf-8") as file:
    data = json.load(file)  

print(json.dumps(data[5], indent=4))