def get_common_questions():
    return {
        "What should I include in a resume?": 
            "Include contact info, a professional summary, skills, work experience, and education.",
        "How long should my resume be?": 
            "1 page for most roles; 2 pages max if you have a lot of experience.",
        "What file format should I use?": 
            "PDF is preferred by most employers."
    }

def job_search_mock(location):
    return [
        {"title": "Customer Service Rep", "company": "ABC Corp"},
        {"title": "Remote Data Entry Clerk", "company": "DataFix"},
        {"title": "Retail Associate", "company": "SuperMart"}
    ]

def interview_mock():
    return {
        "Tell me about yourself.": 
            "Craft a 1-2 minute story focusing on your background and key strengths related to the role.",
        "What are your strengths?": 
            "Mention 2-3 strengths with examples of how you've used them in the past.",
        "Why should we hire you?": 
            "Summarize how your experience and values align with the company and job role."
    }
