import pypdf
from pypdf import PdfReader


def extractincidents(incident_data):
    reader = PdfReader("example.pdf")
    page = reader.pages[0]
    print(page.extract_text()) # Shows the extracted text