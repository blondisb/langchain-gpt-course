from app.mymodules.mylangchain import proccess_pdf
from fastapi import FastAPI, File, UploadFile, HTTPException
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
    print(file.filename)
    resp = proccess_pdf(file.filename)
    
    return {"filename": file.filename, "text": resp}







# - - -
@app.get("/download/{filename}")
async def download_pdf(filename: str):
    # Check if the requested file exists
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Return the PDF file as response
    return FileResponse(filename, media_type='application/pdf')

















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

