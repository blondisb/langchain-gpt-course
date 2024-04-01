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




# - - -
@app.get("/emb/")
def emb():
    docs = [
        """Notificaciones electr�nicas: fabi94_8@hotmail.com 
        3143072390   
        Su causa, es la nuestra!
        Bucaramanga, 08 de Agosto de 2.023
        Se�ores:
        JAMAR
        DERECHO DE PETICI�N
        FREDY RAFAEL MOLINA GAMEZ, mayor de edad, ciudadano colombiano, actualmente en ejercicio, 
        identific�ndome con la c�dula de ciudadan�a No. 85470326, obrando en mi propio nombre y 
        representaci�n de forma respetuosa y haciendo uso de mi derecho fundamental a la petici�n contemplado 
        como tal en el art�culo 23 de la Norma Supe rior, acudo ante usted con el fin de exponer, narrar y solicitar 
        lo siguiente:""",
        """FUNDAMENTOS DE HECHO Y DERECHO
        Colombia al ser un estado social de derecho, garantiza a todos sus ciudadanos el desarrollo de todos sus 
        derechos y protege m�s a�n cuando de derechos fundamentales se trata, por ello en el art�culo 29 de la 
        Constituci�n pol�tica establece el debido proceso en toda actuaci�n, y, a su vez, el art�culo 12 de la ley 
        1266 de 2.008 establece la notificaci�n previa al reporte negativo en centrales, de no ser as� estar�an 
        vulnerando mis derechos fundamentales al debido proceso, h�beas data, buen nombre. """,
        """PRETENSIONES
        PRIMERA: Debido a lo narrado en el ac�pite de hechos solicito de manera respetuosa me sea enviada 
        copia original del contrato � document o equivalente que suscrib� con su entidad. """,
        """Notificaciones electr�nicas: fabi94_8@hotmail.com 
        3143072390   
        Su causa, es la nuestra!
        SEGUNDA: En aplicaci�n a lo ordenado en el art�culo 4� A de la ley 1266 de 2.008 se me expida e informe 
        que los datos en mi contra reportados son veraces, completos, exactos y actualizados. �Cu�ndo fue la 
        �ltima actualizaci�n?
        TERCERA :Informar y se me explique c�mo su entidad cumple con lo reglado en el art�culo 4.B de la ley 
        1266 de 2.008, esto es la finalidad del tratamiento de datos personales, �cu�ndo y en qu� forma me fue 
        informado como titular?  Solicito sea comprobado
        CUARTA :Solicito copia del documento donde se evidencie la autorizaci�n y mi firma para enviar 
        informaci�n a centrales de riesgo, de conformidad con los art�culos 6, literal 2.3 y 8.5 de la ley 1266 de 
        2008.
        QUINTA : Solicito copia de la notificaci�n previa de la que tratan los art�culos 12 de la ley 1266 de 2.008, 
        2 del Decreto 2952 de 2010, 1.3.6. de la resoluci�n 76434 de 2.012 expedida por la Superintendencia de 
        Industria y comercio.
        Con la respectiva constancia de env�o de la comunicaci�n a mi domicilio, con la autorizaci�n de la 
        empresa de mensajer�a que est� autorizada para tal fin.
        SEXTA: En caso de que se haya realizado la notificaci�n previa por un medio distinto demostrar que as� 
        lo establecimos previamente, de conformidad con lo dispuesto en el art�culo 1.3.6. literal b, de la 
        resoluci�n 76434 de 2.012 expedida por la SIC.Con la respectiva constancia de env�o de la comunicaci�n 
        a mi domicilio, con la autorizaci�n de la empresa de mensajer�a que est� autorizada para tal fin.
        S�PTIMA :Si la entidad no ostenta esta obligaci�n remitirla a qui�n competa de conformidad con el 
        art�culo 21 de la ley 1755 de 2.015
        OCTAVA: En caso de que mi obligaci�n haya sido vendida, cedida, o por cualquier tr�mite entregada a 
        otra entidad, copia de la notificaci�n realizada a mi de est� cesi�n para que surja efectos, de conformidad 
        con el art�culo 888 del c�digo de comercio y 1959 del c�digo civil .
        NOVENA : Se me informe y compruebe la fecha exacta en que se hizo el reporte, con el fin de verificar 
        que si se efectu� en los t�rminos de ley; es decir que haya sido reportada la informaci�n vencido los 20 
        d�as de los que tratan los art�culos 12 de la ley 1266 de 2.008 y el 1.3.6. de la resoluci�n 76434 de 2.012 
        expedida por la Superintendencia de Industria y comercio"""
    ]
    return {"message": test_embb(docs)}











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