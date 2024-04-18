import os
# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv


openai_api_key = os.getenv("OPENAI_API_KEY")
load_dotenv(find_dotenv(), override=True)
os.environ.get('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("OpenAI API key not found in environment variable OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
# Did not find openai_api_key, please add an environment variable `OPENAI_API_KEY` which contains it, or pass `openai_api_key` as a named parameter. (type=value_error)