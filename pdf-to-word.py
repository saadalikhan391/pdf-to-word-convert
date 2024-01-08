# Import Libraries
from pdf2docx import parse
from typing import Tuple

#Let's define the function responsible for converting PDF to Docx:
def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    """Converts pdf to docx"""
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=pages)
    summary = {
        "File": input_file, "Pages": str(pages), "Output File": output_file
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result

#The convert_pdf2docx() function allows you to specify a range of pages to convert, it converts a PDF file into a Docx file and prints a summary of the conversion process in the end.

if __name__ == "__main__":
    import sys
    input_file = "about-python.pdf"
    output_file = "about-python.docx"
    convert_pdf2docx(input_file, output_file)

#We simply use Python's built-in sys module to get the input and output file names from command-line arguments. Let's try to convert a sample PDF file
    