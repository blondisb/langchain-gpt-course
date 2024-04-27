from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain

# Mixing classess
class StreamingConversationalRetrievalChain(
    StreamableChain,
    ConversationalRetrievalChain
):
    pass