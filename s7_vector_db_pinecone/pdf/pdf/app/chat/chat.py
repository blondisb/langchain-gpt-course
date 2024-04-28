from langchain.chains import ConversationalRetrievalChain
from app.chat.models import ChatArgs
from app.chat.vectorstores.pinecone import build_retriever
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain


def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    retriever = build_retriever(chat_args)
    llm = build_llm(chat_args)
    memory = build_memory(chat_args)

    try:
        print("\n-----------------------------ConversationalRetrievalChain.from_llm")
        # return ConversationalRetrievalChain.from_llm(
        return StreamingConversationalRetrievalChain.from_llm(
            llm=llm,
            memory=memory,
            retriever=retriever
        )
    except Exception as e:
        filename = './error.txt'
        try:
            with open(filename, 'w',  encoding="utf-8") as file:
                file.write(e)
            print("String successfully exported to", filename)
        except IOError:
            print("Error: Unable to write to file", filename)
        raise Exception("\n----------------\n An error ocurred"+str(e)) from e
