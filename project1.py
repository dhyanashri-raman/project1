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

        print(about)
        file.write("| " + school + "| " + degree + "| " + position + "| " + about + "\n")      