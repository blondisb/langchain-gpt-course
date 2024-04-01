from app.mymodules.manage_files import export_string_to_txt, delete_folder, json_touch
import os
from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAI
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
from openai import OpenAI




load_dotenv(find_dotenv(), override=True)
os.environ.get('OPENAI_API_KEY')
client = OpenAI()

model_setted = ChatOpenAI()
embeddings = OpenAIEmbeddings()

# llm = OpenAI()


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
        # context = """
        #     Eres un abogado experto en leyes colombianas.
        #     Cada pretencion legal debe tener al menos 80 caracteres. Ejemplo: "PRIMERA: Debido a lo narrado en el acápite de hechos solicito de manera respetuosa me sea enviada copia original del contrato que suscribí con su entidad."
        #     Las pretenciones pueden iniciar con palabras como: "PRIMERA", "SEGUNDA", "TERCERA", etcetera.
        #     Si hay pretenciones, las vas a entregar en una lista de python.Ejemplo: ['pretencion_primera', 'pretencion_segunda', 'pretencion_tercera', etcetera].
        #     Si no hay pretenciones, responde NO HAY pretenciones.
        #     En el siguiente documento vas a buscar PRETENCIONES o PETICIONES.
        #     """
        
        context = "En una lista de python, clasifica las pretenciones detalladamente del parrafo que te enviare. SI no hay, coloca NO HAY."

        template = ChatPromptTemplate.from_messages([
            ("system", context),
            ("human", "{user_input}")
        ])

        code_chain = LLMChain(
            llm=client, #llm,
            prompt=template,
            output_key='json_partial'
        )

        result_chain = code_chain({'user_input': str(doc)})

        if 'NO HAY PRETENCIONES' in result_chain['json_partial']:
           print('XXX')
           return 'pass'
        
        # result = json_touch(result_chain['json_partial'])
        return  result_chain['json_partial']
    
    except Exception as e:
        print(e)
        raise Exception("An error occurred") from e


def chat_prompt_openai(doc):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en leyes colombianas. Vas a buscar unicamente pretenciones."},
            {"role": "user", "content": f"Enumerame estas pretenciones en formato json, si no hay, responde NO HAY PRETENCIONES. Parrafo: {doc}"}
        ]
    )

    print(completion.choices[0].message.content)
    print(type(completion.choices[0].message.content))
    return (str(completion.choices[0].message.content))


def test_embb(docs):
    for index, doc in enumerate(docs):

        export_string_to_txt(
            doc.page_content,
            f"C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/txt/input_{index}.txt"
        )

        json = chat_prompt_openai(str(doc.page_content))
        if json == 'pass':
           continue

        export_string_to_txt(
            json,
            f"C:/Mega/Courses/Langchain_course/Jamar/project04/Outs/json/output_{index}.txt"
        )
        time.sleep(3.2)
        break
    return 'OK'
