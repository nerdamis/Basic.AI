import re

def get_resume_tips(resume_text):
    tips = []
    if not re.search(r"\bexperience\b", resume_text, re.IGNORECASE):
        tips.append("Add a section for work experience.")
    if not re.search(r"\beducation\b", resume_text, re.IGNORECASE):
        tips.append("Make sure your education is listed.")
    if len(resume_text.split()) < 150:
        tips.append("Your resume looks too short.")
    return tips