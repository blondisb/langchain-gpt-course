from app.mymodules.manage_files import export_string_to_txt, delete_folder, json_touch
import os
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings.base import Embeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import BaseRetriever
from langchain.chains import RetrievalQA
from langchain.schema import SystemMessage
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv, find_dotenv
import time
from langchain_core.prompts import ChatPromptTemplate


load_dotenv(find_dotenv(), override=True)
os.environ.get('OPENAI_API_KEY')


model_setted = ChatOpenAI()
embeddings = OpenAIEmbeddings()

llm = OpenAI()


class RedundantFilterRetriever(BaseRetriever):
  embeddings: Embeddings
  chroma: Chroma

  def get_relevant_documents(self, query):
    #calculate embeddings for the query string
    emb = self.embeddings.embed_query(query)
    #take embeddings and feed them into that
    #max_marginal_relevance_search_by_vector (remove duplicates)
    return self.chroma.max_marginal_relevance_search_by_vector(
        embedding=emb,
        lambda_mult=0.8
    )

  async def aget_relevant_documents(self):
    return[]

def save_embs(docs, prompt):
    delete_folder("C:/Mega/Courses/Langchain_course/Jamar/project04/emb1")
    
    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory="emb1"
    )

    # retriever = RedundantFilterRetriever(
    #     embeddings=embeddings,
    #     chroma=db
    # )

    # chain = RetrievalQA.from_chain_type(
    #     llm=model_setted,
    #     retriever=retriever,
    #     chain_type="stuff"
    # )
    # return chain 

    results = db.similarity_search_with_score(
        prompt,
        k=5 #two relevants results. Default is 4.
    )

    return results


def chat_prompt(doc):

    try:
        context = """
            Eres un abogado experto en leyes colombianas.
            Cada pretencion legal debe tener al menos 80 caracteres. Ejemplo: "PRIMERA: Debido a lo narrado en el acápite de hechos solicito de manera respetuosa me sea enviada copia original del contrato que suscribí con su entidad."
            Las pretenciones pueden iniciar con palabras como: "PRIMERA", "SEGUNDA", "TERCERA", etcetera.
            """
        
        prompt_p1 = """Te voy a dar un parrafo. Lo analizas.
            Si no hay pretenciones, responde NO_HAY_PRETENCIONES.
            Si hay pretenciones, las vas a entregar en una lista de python.Ejemplo: ['pretencion_primera', 'pretencion_segunda', 'pretencion_tercera', etcetera].
            El parrafo es: """
        

        template = ChatPromptTemplate.from_messages([
            ("system", context),
            ("human", prompt_p1+'"{user_input}"')
        ])

        code_chain = LLMChain(
            llm=llm,
            prompt=template,
            output_key='json_partial'
        )

        result_chain = code_chain({'user_input': str(doc)})

        if 'NO_HAY_PRETENCIONES' in result_chain['json_partial']:
           print('XXX')
           return 'pass'
        
        # result = json_touch(result_chain['json_partial'])
        return  result_chain['json_partial']
    
    except Exception as e:
        print(e)
        raise Exception("An error occurred") from e
