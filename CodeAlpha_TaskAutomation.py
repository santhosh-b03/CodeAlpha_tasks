import streamlit as st
import re
import os

st.title("Email Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file is not None:
    # Read file content
    text = uploaded_file.read().decode("utf-8")

    # Extract emails
    emails = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    )

    if emails:
        st.success("Email addresses found!")

        # Save emails to txt file in same folder
        with open("emails.txt", "w") as file:
            for email in emails:
                file.write(email + "\n")
        st.write("Extracted Emails:")
        for email in emails:
            st.write(email)

        st.info("Emails saved successfully in emails.txt")

    else:
        st.warning("No email addresses found.")
