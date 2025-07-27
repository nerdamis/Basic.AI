import streamlit as st
from resume_editor import get_resume_tips
from utils import get_common_questions, job_search_mock, interview_mock

st.set_page_config(page_title="JobBot", layout="centered")
st.title("🤖 JobBot – Your AI Career Assistant")

menu = st.sidebar.selectbox("Navigate", ["Home", "Resume Help", "Job Search", "Interview Prep"])

if menu == "Home":
    st.markdown("Welcome to **JobBot**! Use the sidebar to explore features that help you succeed in your job hunt.")

elif menu == "Resume Help":
    st.header("📄 Resume Help")
    uploaded = st.file_uploader("Upload your resume (.txt)", type=["txt"])
    if uploaded:
        resume_text = uploaded.read().decode("utf-8")
        st.subheader("AI Feedback:")
        tips = get_resume_tips(resume_text)
        for tip in tips:
            st.write("- " + tip)

    st.subheader("Common Resume Questions")
    for q, a in get_common_questions().items():
        with st.expander(q):
            st.write(a)

elif menu == "Job Search":
    st.header("🌍 Job Search")
    location = st.text_input("Enter a location (e.g., Omaha, NE):")
    if location:
        jobs = job_search_mock(location)
        st.write(f"Found {len(jobs)} jobs in {location}:")
        for job in jobs:
            st.write(f"- **{job['title']}** at *{job['company']}*")

elif menu == "Interview Prep":
    st.header("🎤 Interview Practice")
    st.markdown("Below are common questions. Think your answers through, or click to reveal suggestions.")
    for q, a in interview_mock().items():
        with st.expander(q):
            st.write(a)
