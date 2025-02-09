import json
import re
from docx import Document

# Paths for input and output files
input_file = '/Users/omarelmokhtarelboussouni/Desktop/faroukProject/rawData.docx'
output_file = 'data.json'

data = []

# Function to read DOCX file and extract text
def read_docx(file_path):
    doc = Document(file_path)
    return [p.text for p in doc.paragraphs if p.text.strip()]

# Regex pattern to extract question and answer
pattern = r'^(.*?):\s*\{(.*?)\}$'

# Read and parse the DOCX file
lines = read_docx(input_file)
for line in lines:
    match = re.match(pattern, line.strip())
    if match:
        question, answer = match.groups()
        data.append({
            "question": question.strip(),
            "answer": answer.strip()
        })

# Write data to a JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON data has been written to {output_file}")