from app.mymodules.get_pdf import proccess_pdf
from app.mymodules.gen_pdf import generate_pdf
from app.mymodules.gen_result import test_embb
from fastapi import FastAPI, File, UploadFile, HTTPException, Response
from starlette.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}



# - - -
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Save the uploaded PDF file
    with open(file.filename, "wb") as pdf:
        pdf.write(await file.read())
    
    # Process the PDF using langchain and PyPDF2
    resp = proccess_pdf(file.filename)
    
    return {"filename": file.filename, "text": resp}







# - - -
@app.get("/download/{filename}")
async def download_pdf(filename: str, response: Response):
    # Generate the PDF file content
    pdf_content = generate_pdf()

    # Set response headers to force download
    response.headers["Content-Disposition"] = f"attachment; filename=output_{filename}"
    response.headers["Content-Type"] = "application/pdf"

    # Save the PDF content to a file
    PDF_FOLDER ="C:/Mega/Courses/Langchain_course/Jamar/project04/app/media"
    file_path = os.path.join(PDF_FOLDER, filename)
    with open(file_path, "wb") as pdf_file:
        pdf_file.write(pdf_content)

    # Return the PDF content
    return Response(content=pdf_content, media_type="application/pdf")








# ____________________________________________________________________________________
# def process_pdf(pdf_path):
#     # Extract text from PDF using PyPDF2
#     with open(pdf_path, "rb") as pdf_file:
#         pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#         text = ""
#         for page_num in range(pdf_reader.numPages):
#             page = pdf_reader.getPage(page_num)
#             text += page.extractText()
    
#     # Use langchain to process the text
#     # lc = LanguageChain()
#     # processed_text = lc.process(text)
    
#     return "processed_text"




# @app.get("/download/{filename}")
# async def download_pdf(filename: str):
#     # Generate the PDF file
#     string_list = ["First page", "Second page", "Third page"]
#     generate_pdf(string_list, f"C:/Mega/Courses/Langchain_course/Jamar/project04/app/media/output_{filename}.pdf")

#     # Check if the requested file exists
#     if not os.path.exists(filename):
#         raise HTTPException(status_code=404, detail="File not found")
    
#     # Return the PDF file as response
#     return FileResponse(filename, media_type='application/pdf')