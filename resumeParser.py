import PyPDF2
def extract_content(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"  
    return text.strip()

def extract_skills(resume_text):
    skill_keywords = ["Python", "Machine Learning", "Deep Learning", "C++", "Java",
                      "AWS", "Cloud", "Data Science", "Cybersecurity", "NLP", "JavaScript"]
    return [skill for skill in skill_keywords if skill.lower() in resume_text.lower()]