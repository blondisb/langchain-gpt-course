from functools import partial
from .pinecone import build_retriever

# Three setups for retriever fetchs 1 or 2 or 3 relevant docs
retriever_map = {
    "pinecone_1": partial(build_retriever, k=1),
    "pinecone_2": partial(build_retriever, k=2),
    "pinecone_3": partial(build_retriever, k=3)
}