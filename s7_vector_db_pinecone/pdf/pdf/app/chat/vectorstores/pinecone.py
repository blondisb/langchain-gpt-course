import os
import pinecone
# from langchain.vectorstores import Pinecone
# from langchain_community.vectorstores import Pinecone
from langchain_pinecone import PineconeVectorStore
from app.chat.embeddings.openai import embeddings

# pinecone.init(
#     api_key=os.getenv("PINECONE_API_KEY"),
#     environment=os.getenv("PINECONE_ENV_NAME")
# )

# vector_store = PineconeVectorStore.from_existing_index(
#     os.getenv("PINECONE_INDEX_NAME"), embeddings
# )

# vectorstore = PineconeVectorStore(
#     index_name=os.getenv("PINECONE_INDEX_NAME"),
#     embedding=embeddings
# )

def call_vector_store(docs):
    vectorstore_from_docs = PineconeVectorStore.from_documents(
        docs,
        index_name=os.getenv("PINECONE_INDEX_NAME"),
        embedding=embeddings
    )

vectorstore = PineconeVectorStore(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings
) 

def build_retriever(chat_args):
    search_kwards = {"filter": {"pdf_id": chat_args.pdf_id }}
    return vectorstore.as_retriever(search_kwards=search_kwards)
