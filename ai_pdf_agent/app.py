import streamlit as st
from pdf_extractor import extract_text_from_pdf
from question_processor import find_answers
from llm_query import query_openai_model

st.title("PDF Question Answering Agent")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
questions_input = st.text_area("Enter your questions (one per line):")

if st.button("Submit"):
    if uploaded_file is not None and questions_input:
        # Save the uploaded PDF to a temporary location
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the questions
        questions_list = questions_input.splitlines()

        # Extract text from the PDF
        text = extract_text_from_pdf("temp.pdf")

        # Find answers to the questions
        answers = find_answers(text, questions_list)
        for question, answer in answers.items():
            if answer == "Data Not Available":
                prompt = f"Given the following text: '{text[:2000]}', answer this question: '{question}'"
                answers[question] = query_openai_model(prompt)

        # Display the results
        for question, answer in answers.items():
            st.write(f"**Q: {question}**")
            st.write(f"A: {answer}")
    else:
        st.warning("Please upload a PDF and enter your questions.")
