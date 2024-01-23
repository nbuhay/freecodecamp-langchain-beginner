import langchain_helper as lch
import streamlit as st

st.title("SecVuln Solution Generator")

famous_vulnerabilities = ', '.join([
    "CVE-2014-0160 (Heartbleed)",
    "Log4J CVE-2021-44228 (Log4J)" ])

question = "What vulnerabilitiy do you need to fix? " \
"Try famous vulnerabilites like {}".format(famous_vulnerabilities)

user_vuln = st.sidebar.text_area(question)

if user_vuln:
    response = lch.gen_vulnerabilitiy_fix(user_vuln)
    st.text(response)