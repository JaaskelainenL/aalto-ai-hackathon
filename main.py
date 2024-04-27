from openai import OpenAI
from PyPDF2 import PdfReader
from datetime import datetime
import docx
import os
import sys

CHARACTER_LIMIT = 5000

if len(sys.argv) != 2:
        print("Usage: python main.py FILENAME")
        sys.exit(1)  # Exit with error

FILENAME = sys.argv[1]




with open("apikey.txt") as f:
    KEY = f.read().strip()

client = OpenAI(api_key=KEY)

def readPdf(filename):
    reader = PdfReader(filename) 
    txt = ""

    for page in reader.pages:
        txt += page.extract_text()

    return txt


def readDocx(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)




content = ""

filetype = os.path.splitext(FILENAME)[1:] 


if filetype[0].lower() == ".pdf":
  content = readPdf(FILENAME)
elif filetype[0].lower() == ".docx":
  content = readDocx(FILENAME)
else:
  exit("Invalid file type")





response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You work at Hanshin Solutions. We manifacture kitchen sink plugs and 45 angle degree corner pipes. Nothing more nothing less. Kitchen sink plugs cost $10 a piece because they are premium quality. The 45 angle degree corner pipes cost $100 a piece."},
    {"role": "system", "content": "You are supposed to evaluate the given Request For Proposal. Make a json of your awnsers."},
    {"role": "system", "content": "Who sent the proposal (call the key name)?"},
    {"role": "system", "content": "What are their contact information (call the key contact)?"},
    {"role": "system", "content": "What is their address (call the key address)? "},
    {"role": "system", "content": "Give me a briefing of the content (call the key briefing)."},
    {"role": "system", "content": "Which of our product would be suitable if none awnser null (call the key product)?"},
    {"role": "system", "content": "What price does the customer want, awnser this in a number format (call the key price)?"},
    {"role": "system", "content": "How many pieces does the customer want awnser in a number format (call the key pieces)?"},
    {"role": "system", "content": "Is the price over or under our production costs awnser as true or false (true being over) (call the key worth_it)?"},


    {"role": "system", "content": "Your awnser must only be the JSON. Do not include markdown or anything else."},
    {"role": "user", "content": content[:CHARACTER_LIMIT]},
    
  ]
)
message_content = response.choices[0].message.content


date = datetime.now().strftime("%Y-%m-%d")

with open(FILENAME+"-analysis-"+date+".json", 'w') as file:
    file.write(message_content)