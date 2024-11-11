import re
import spacy

nlp = spacy.load("en_core_web_sm")

def find_answers(text, questions):
    """Finds answers to questions from the text."""
    answers = {}
    for question in questions:
        answer = search_text_for_answer(text, question)
        if not answer:
            answers[question] = "Data Not Available"
        else:
            answers[question] = answer
    return answers

def search_text_for_answer(text, question):
    """Performs basic keyword matching and extracts relevant parts."""
    doc = nlp(text)
    if question.lower() in text.lower():
        match = re.search(re.escape(question), text, re.IGNORECASE)
        if match:
            start = max(0, match.start() - 50)
            end = min(len(text), match.end() + 50)
            return text[start:end].strip()
    return None
