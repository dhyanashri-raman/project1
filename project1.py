import json

with open("LinkedInProfiles.json", "r", encoding="utf-8") as file:
    data = json.load(file)  

with open("names.txt", "w", encoding="utf-8") as file:
    for line in data:
        name = line.get("name", None)  
        if name is None:
            continue
        print(name)
        file.write(name + "\n")
        

# with open("output.txt", "w", encoding="utf-8") as file:
#     json.dump(random_entry, file, indent=4)