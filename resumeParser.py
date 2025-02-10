import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"  # Extract text from each page
    return text.strip()

# Example usage
pdf_resume = "resume.pdf"  # Replace with your actual file
resume_text = extract_text_from_pdf(pdf_resume)

print(resume_text)  # View extracted text
