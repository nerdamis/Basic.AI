import streamlit as st
from resume_editor import get_resume_tips

st.title("JobBot - Your Career Assistant")

query = st.text_input("Ask me something about resumes, jobs, or interviews:")
if query:
    if "resume" in query.lower():
        tips = get_resume_tips("sample resume text here")
        st.write("Resume Tips:")
        for tip in tips:
            st.write("- " + tip)
    else:
        st.write("I'm still learning, but try asking about resume improvements!")