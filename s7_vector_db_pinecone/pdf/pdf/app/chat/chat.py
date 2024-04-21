from app.chat.models import ChatArgs
from app.chat.vectorstores.pinecone import build_retriever

def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """

    def buil_chat(chat_args: ChatArgs):
        retriever = build_retriever(chat_args)

    pass
