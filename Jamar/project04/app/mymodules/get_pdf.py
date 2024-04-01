from app.mymodules.gen_result import test_embb
from app.mymodules.manage_files import delete_contents_of_folder, export_string_to_txt
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import  CharacterTextSplitter

def proccess_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
                    "HECHOS",
                    "FUNDAMENTOS DE HECHO Y DERECHO",
                    "PRETENSIONES",
                    "NOTIFICACIONES"
                    ],
        chunk_size=100,
        chunk_overlap=0
    )
    
    docs = loader.load_and_split(text_splitter)    

    # # Call the function to delete contents of the folder
    delete_contents_of_folder("C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/json")
    delete_contents_of_folder("C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/txt")

    # return "Proccessed"
    return {"message": test_embb(docs)}

