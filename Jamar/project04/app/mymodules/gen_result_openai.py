import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

load_dotenv(find_dotenv(), override=True)
os.environ.get('OPENAI_API_KEY')
client = OpenAI()



def chat_prompt_openai(doc):

    system = """ Este es un ejemplo de como me debes entregar las respuestas:
        {
        "pretenciones": [
            {
            "numero": "TERCERA",
            "descripcion": "Solicitar copia de la notificación previa de la que tratan los artículos 12 de la ley 1266 de 2008, del Decreto 2952 de 2010, 1.3.6 de la resolución 76434 de 2012 expedida por la Superintendencia de Industria y Comercio."
            },
            {
            "numero": "CUARTA",
            "descripcion": "En caso de que la entidad no ostente esta obligación, solicitar que sea remitida a quien competa de acuerdo con el artículo 21 de la ley 1755 de 2015."
            },
            {
            "numero": "QUINTA",
            "descripcion": "En caso de que la obligación haya sido vendida, cedida o entregada a otra entidad, solicitar copia de la notificación realizada sobre esta cesión, de acuerdo con el artículo 888 del código de comercio y el artículo 1959 del código civil."
            }
        ]
        }"""
    
    human = """ Te voy a dar un parrafo. Analizalo.
        Si no tiene pretenciones responde NO_HAY_PRETENCIONES.
        Caso contrario, entregame las pretenciones en formato JSON estandar."""

    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": human+doc}
        ])

    if 'NO_HAY_PRETENCIONES' in str(completion.choices[0].message.content):
        return 'pass'

    return str(completion.choices[0].message.content)