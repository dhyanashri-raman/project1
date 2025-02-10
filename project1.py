import json
import openai
import os
import time

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
        fields = line.strip().split("| ")
        
        name = fields[0] if len(fields) > 0 and fields[0] != "NoField" else "Unknown"
        location = fields[1] if len(fields) > 1 and fields[1] != "NoField" else "Unknown"
        company = fields[2] if len(fields) > 2 and fields[2] != "NoField" else "Unknown"
        university = fields[3] if len(fields) > 3 and fields[3] != "NoField" else "Unknown"
        degree = fields[4] if len(fields) > 4 and fields[4] != "NoField" else "Unknown"
        position = fields[5] if len(fields) > 5 and fields[5] != "NoField" else "Unknown"
        about = fields[6] if len(fields) > 6 and fields[6] != "NoField" else "Unknown"

        profiles.append({
            "name": name,
            "location": location,
            "company": company,
            "university": university,
            "degree": degree,
            "position": position,
            "about": about
        })

    with open("prompts.txt", "w", encoding="utf-8") as file3:
        count = 0
        for profile in profiles:
            if count == 0:
                count += 1
                continue
            prompt = f"Generate a networking email to {profile['name']}, who works at {profile['company']} as {profile['position']}. {profile['name']} earned their degree, {profile['degree']}, from {profile['university']}. Their About section is: {profile['about']}. Mention that I am interested in learning more about their work and connecting over shared interests in software engineering. Keep the email polite, engaging, and professional."
            file3.write(prompt + "\n")

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load the API key

with open("prompts.txt", "r", encoding="utf-8") as file:
    prompts = file.readlines()

def generate_email(prompt):
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-4-turbo",  # Need to replace with the o-1 mini model
                messages=[
                    {"role": "system", "content": "You are an AI that generates professional networking emails."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()

        except openai.RateLimitError:
            print("Rate limit reached. Waiting 10 seconds before retrying...")
            time.sleep(10) 

        except Exception as e:
            print(f"Error: {str(e)}")
            return None

with open("networking_emails.txt", "w", encoding="utf-8") as output_file:
    for i, prompt in enumerate(prompts):
        prompt = prompt.strip()
        if prompt:
            email = generate_email(prompt)
            if email:
                output_file.write(f"Email {i+1}:\n{email}\n\n{'='*80}\n\n")
                print(f"Generated email {i+1} successfully.")

print("\n All emails have been generated and saved to 'networking_emails.txt'.")
