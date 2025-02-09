import streamlit as st
import json
from fuzzywuzzy import fuzz

# Load the JSON file
import os
json_file = os.path.join(os.path.dirname(__file__), 'data.json')

with open(json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Streamlit app interface
st.title("Question Answer Finder")

# User input
user_question = st.text_input("Enter your question:")

# Threshold for fuzzy matching
match_threshold = 95  # Keep only exact or very close matches

if user_question:
    # Find all matching answers with high similarity
    matching_answers = []
    for item in data:
        similarity_score = fuzz.partial_ratio(item['question'].lower(), user_question.lower())
        if similarity_score >= match_threshold:
            matching_answers.append(item['answer'])

    # Display results
    if matching_answers:
        st.write("### Answers found:")
        for idx, answer in enumerate(matching_answers, start=1):
            st.write(f"{idx}. {answer}")
    else:
        st.write("No matching answers found.")
