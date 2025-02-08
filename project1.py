import json

with open("LinkedInProfiles.json", "r", encoding="utf-8") as file:
    data = json.load(file)  

with open("names.txt", "w", encoding="utf-8") as file:
    file.write("name | city | company | college | degree | position | about \n")
    for line in data:
        name = line.get("name", None)  
        city = line.get("city", None)
        company = line.get("current_company", "")
        if company != "":
            company = company.get("name", "NoField")

        if name is None:
            continue
        file.write(name + "| " + city + "| " + company)

        #school name and degree
        school = line.get("educations_details", "NoField")
        education_details = line.get("education", "NoField")

        if education_details == None:
            education_details = "NoField"
        else:
            degree = education_details[0].get("degree", "NoField")

        about = line.get("about", "")
        position = line.get("position", "")
        if position == "":
            position = "NoField"
        if about == "":
            about = "NoField"

        file.write("| " + school + "| " + degree + "| " + position + "| " + about + "\n")     

with open("names.txt", "r", encoding="utf-8") as file2:
    lines = file2.readlines()

    profiles = []
    for line in lines:
        fields = line.strip().split("|")
        
        name = fields[0] if len(fields) > 0 and fields[0] != "NoField" else "Unknown"
        location = fields[1] if len(fields) > 1 and fields[1] != "NoField" else "Unknown"
        company = fields[2] if len(fields) > 2 and fields[2] != "NoField" else "Unknown"
        university = fields[3] if len(fields) > 3 and fields[3] != "NoField" else "Unknown"
        degree = fields[4] if len(fields) > 4 and fields[4] != "NoField" else "Unknown"
        position = fields[5] if len(fields) > 5 and fields[5] != "NoField" else "Unknown"
        about = fields[6] if len(fields) > 6 and fields[6] != "NoField" else "NoAbout"

        profiles.append({
            "name": name,
            "location": location,
            "company": company,
            "university": university,
            "degree": degree,
            "position": position,
            "about": about
        })

    # Print extracted data
    for profile in profiles:
        print(profile)
    