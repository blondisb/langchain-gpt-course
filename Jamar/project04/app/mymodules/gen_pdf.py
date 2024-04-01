# Import required libraries
# from app.mymodules.gen_result import generate_response
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger, PdfReader
import io


def generate_pdf():
    # Create a BytesIO buffer to hold PDF content
    pdf_buffer = io.BytesIO()

    # Create a new PDF canvas
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Write text to the PDF canvas
    c.drawString(100, 750, "Hello, this is a dynamically generated PDF!")

    # Save the PDF canvas content
    c.save()

    # Get the PDF content from the buffer
    pdf_content = pdf_buffer.getvalue()
    
    return pdf_content











def generate_pdf2(string_list, output_filename):
    # Create a BytesIO buffer to hold PDF content
    pdf_buffer = io.BytesIO()

    # Create a new PDF canvas
    c = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Write each string from the list to the PDF canvas
    y_position = 750  # Initial y position
    for string in string_list:
        c.drawString(100, y_position, string)
        y_position -= 12  # Move the y position up for the next line
    
    # Save the PDF canvas content
    c.save()

    # Get the PDF content from the buffer
    pdf_content = pdf_buffer.getvalue()
    
    # Write the PDF content to a file
    with open(output_filename, 'wb') as f:
        f.write(pdf_content)




def merge_pdfs(input_files, output_filename):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Append each PDF file to the merger
    for input_file in input_files:
        merger.append(PdfReader(input_file))

    # Write the merged PDF to the output file
    merger.write(output_filename)


# Example usage:
# string_list = ["First page", "Second page", "Third page"]
# generate_pdf(string_list, f"C:/Mega/Courses/Langchain_course/Jamar/project04/app/media/output.pdf")

# If you have multiple PDF files to merge:
# input_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
# merge_pdfs(input_files, "merged_output.pdf")
