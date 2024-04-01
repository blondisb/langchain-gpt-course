from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import  CharacterTextSplitter
import shutil
import os



def export_string_to_txt(string_to_export, filename):
    try:
        with open(filename, 'w') as file:
            file.write(string_to_export)
        print("String successfully exported to", filename)
    except IOError:
        print("Error: Unable to write to file", filename)

def delete_contents_of_folder(folder_path):
    # Iterate over all the files and subdirectories in the folder
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            # Delete each file
            file_path = os.path.join(root, name)
            os.remove(file_path)
        for name in dirs:
            # Delete each subdirectory
            dir_path = os.path.join(root, name)
            shutil.rmtree(dir_path)


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

    # export_string_to_txt(str(loader.load()), "output.txt")

    docs = loader.load_and_split(text_splitter)
    print(len(docs))

    # Call the function to delete contents of the folder
    delete_contents_of_folder("C:\Mega\Courses\Langchain_course\Jamar\project04\Outs")
    for index, doc in enumerate(docs):
        print(doc.metadata)
        export_string_to_txt(str(doc.page_content), f"C:\Mega\Courses\Langchain_course\Jamar\project04\Outs\output{str(index)}.txt")

    
    # export_string_to_txt(str(docs[1].page_content), f"output{1}.txt")
    # export_string_to_txt(str(docs[2].page_content), f"output{2}.txt")
    # export_string_to_txt(str(docs[3].page_content), f"output{3}.txt")

    return "Proccessed"

