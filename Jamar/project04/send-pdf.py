import requests

aa = input()


if aa == '1':
    # Replace the URL with the URL of your FastAPI endpoint
    upload_url = "http://localhost:8000/upload/"

    # Path to the PDF file you want to upload
    # pdf_file_path = "LEGAL-BERT.pdf"
    pdf_file_path = "C:/Mega/Courses/Langchain_course/Jamar/project04/app/media/DERECHO DE PETICION JAMAR - GIAN HERNANDEZ.pdf"
    # pdf_file_path = "C:/Mega/Courses/Langchain_course/Jamar/project04/app/media/derecho de peticion Fredy Molina.pdf"
    # pdf_file_path = "requirements.txt"

    # Open the PDF file in binary mode and send it as part of the request
    with open(pdf_file_path, "rb") as pdf_file:
        files = {"file": pdf_file}
        response = requests.post(upload_url, files=files)

    # Print the response
    print(response.json())




elif aa=='2':
    def download_pdf(filename):
        url = f"http://localhost:8000/download/{filename}"  # Replace with your actual API endpoint URL
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename} successfully.")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")

    # Example usage:
    filename = "example2.pdf"  # Replace with the filename you want to download
    download_pdf(filename)



# elif aa='3':
    
#     {'user_input': "page_content='HECHOS\\nPRIMERO : Al intentar solicitar créditos me aparecen datos negativos reportados por su entidad, lo que \\nme impide acceder y afecta gravemente mis derechos fundamentales al hábeas data, entre otros.\\nSEGUNDO : Esto me produce un perjuicio irremediable, ya que necesito tener mi nombre registrado \\npositivamente en base de datos , con esta información negativa que no es real, no obedece a la verdad \\namenazando gravemente mis derechos fundamentales al hábeas data, debido proceso.\\n' metadata={'source': 'derecho de peticion Fredy Molina.pdf', 'page': 0}", 'json': "\n\nSystem: \n('Pretensiones': ('1': 'Solicitar que se eliminen los datos negativos reportados por su entidad que me impiden acceder a créditos y afectan mis derechos fundamentales al hábeas data.', '2': 'Solicitar una rectificación de la información negativa registrada en las bases de datos, ya que no se ajusta a la realidad y vulnera mis derechos fundamentales al hábeas data y al debido proceso.'))"}
