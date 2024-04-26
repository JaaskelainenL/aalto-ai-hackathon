from PyPDF2 import PdfReader

def readPdf(filename):
    reader = PdfReader(filename) 
    txt = ""

    for page in reader.pages:
        txt += page.extract_text()

    return txt
