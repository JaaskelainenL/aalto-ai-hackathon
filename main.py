from openai import OpenAI
from PyPDF2 import PdfReader

with open("apikey.txt") as f:
    KEY = f.read()

client = OpenAI(api_key=KEY)

def readPdf(filename):
    reader = PdfReader(filename) 
    txt = ""

    for page in reader.pages:
        txt += page.extract_text()

    return txt
