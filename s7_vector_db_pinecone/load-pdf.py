# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
"""
Generate and store embeddings for the given pdf

1. Extract text from the specified PDF.
2. Divide the extracted text into manageable chunks.
3. Generate an embedding for each chunk.
4. Persist the generated embeddings.

:param pdf_id: The unique identifier for the PDF.
:param pdf_path: The file path to the PDF.

Example Usage:

create_embeddings_for_pdf('123456', '/path/to/pdf')
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100 
)

print("\n\n\n")
loader = PyPDFLoader("../spice.pdf")

print(loader)
print("\n\n\n")
docs = loader.load_and_split(text_splitter)
print(docs)

print("\n\n\n")
print(len(docs))



def PINEEECONE():
    import os
    from langchain_pinecone import PineconeVectorStore
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import CharacterTextSplitter
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv(), override=True)


    index_name = "docs"
    embeddings = OpenAIEmbeddings()

    # path to an example text file
    # loader = TextLoader("../../modules/state_of_the_union.txt")
    # documents = loader.load()
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    # docs = text_splitter.split_documents(documents)

    # vectorstore_from_docs = PineconeVectorStore.from_documents(
    #     docs,
    #     index_name=index_name,
    #     embedding=embeddings
    # )

    texts = [
        "Hey loco",
        "que pasa vale mía", 
        "deja de estar mostando las gemelas aqui",
        "acaso tu crees que uno es mk"]

    vectorstore_from_texts = PineconeVectorStore.from_texts(
        texts,
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings
    )

    print(os.getenv("PINECONE_INDEX_NAME"))
    print(vectorstore_from_texts)


print("\n-PINEEECONE--------------------------")
PINEEECONE()
