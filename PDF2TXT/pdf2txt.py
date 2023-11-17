import PyPDF2
import os

# Parse the filename from the path
def get_filename(filepath):
    base = os.path.basename(filepath)
    return os.path.splitext(base)[0]

# Main function, extract the text from the pdf file and write it on a txt file
def pdf_to_txt(pdf_file, txt_file):
    # Open PDF file in binary reading mode
    with open(pdf_file, 'rb') as file:
       from pypdf import PdfReader

    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    with open(txt_file, 'w') as file:
        file.write(text)


filepath='Wordle.pdf'
filename = get_filename(filepath)
filename_txt = f"{filename}.txt"
print(filename)  # Output: test

pdf_to_txt(filepath,filename_txt)
