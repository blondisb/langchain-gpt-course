from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import  CharacterTextSplitter



def export_string_to_txt(string_to_export, filename):
    try:
        with open(filename, 'w') as file:
            file.write(string_to_export)
        print("String successfully exported to", filename)
    except IOError:
        print("Error: Unable to write to file", filename)



def proccess_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
                    # "HECHOS\n"
                    # "FUNDAMENTOS DE HECHO Y DERECHO\n",
                    # "PRETENSIONES\n",
                    # "NOTIFICACIONES\n"
                    ],
        chunk_size=500,
        chunk_overlap=100 
    )

    # export_string_to_txt(str(loader.load()), "output.txt")

    docs = loader.load_and_split(text_splitter)
    print(len(docs))

    for index, doc in enumerate(docs):
        print(doc.metadata)
        export_string_to_txt(str(doc.page_content), f"C:\Mega\Courses\Langchain_course\Jamar\project04\output{str(index)}.txt")

    
    # export_string_to_txt(str(docs[1].page_content), f"output{1}.txt")
    # export_string_to_txt(str(docs[2].page_content), f"output{2}.txt")
    # export_string_to_txt(str(docs[3].page_content), f"output{3}.txt")

    return "Proccessed"

