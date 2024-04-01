import requests

# Replace the URL with the URL of your FastAPI endpoint
upload_url = "http://localhost:8000/upload/"

# Path to the PDF file you want to upload
# pdf_file_path = "LEGAL-BERT.pdf"
pdf_file_path = "C:\Mega\Courses\Langchain_course\Jamar\ddps\DERECHO DE PETICION JAMAR - GIAN HERNANDEZ.pdf"
# pdf_file_path = "requirements.txt"

# Open the PDF file in binary mode and send it as part of the request
with open(pdf_file_path, "rb") as pdf_file:
    files = {"file": pdf_file}
    response = requests.post(upload_url, files=files)

# Print the response
print(response.json())
