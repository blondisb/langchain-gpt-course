from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain

# Mixing classess
class StreamingConversationalRetrievalChain(
    StreamableChain,
    ConversationalRetrievalChain
):
    pass