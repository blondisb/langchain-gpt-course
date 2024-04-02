from app.mymodules.gen_result import test_embb
from app.mymodules.manage_files import delete_contents_of_folder, export_string_to_txt
from app.mymodules.gen_result_openai import chat_prompt_openai
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import  CharacterTextSplitter


async def proccess_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
                    "HECHOS",
                    "FUNDAMENTOS DE HECHO Y DERECHO",
                    "PRETENSIONES",
                    "NOTIFICACIONES"
                    ],
        chunk_size=100,
        chunk_overlap=0)
    
    docs = loader.load_and_split(text_splitter)    

    # # Call the function to delete contents of the folder
    delete_contents_of_folder("C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/json")
    delete_contents_of_folder("C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/txt")

    try:
        # return "Proccessed"
        for index, doc in enumerate(docs):
            export_string_to_txt(
                doc.page_content, f"C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/txt/input_{index}.txt")

            # json = chat_prompt(str(doc.page_content))
            json = chat_prompt_openai(str(doc.page_content))
            if json == 'pass':
                continue

            export_string_to_txt(
                json, f"C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/json/output_{index}.json")
        return {"message": 'OK'}
    
    except Exception as e:
        print(e)
        raise Exception("An error occurred") from e


