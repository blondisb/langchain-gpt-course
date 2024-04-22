from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv
from queue import Queue
from threading import Thread

load_dotenv()

queue = Queue()

class StreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token, **kwargs):
        # print("\ntoken")
        # print(token)
        queue.put(token)

    def on_llm_end(self, response, **kwargs):
        queue.put(None)

    def on_llm_error(self, response, **kwargs):
        queue.put(None)

# control how openAi responds to LangChain 
chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingHandler()]
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

# messages = prompt.format_messages(
#     content="tell me a joke"
# )

# print("\n--------------------")
# print(messages)

# # control how to langchain responds to us
# print("\n--------------------") 
# for message in chat.stream(messages):
#     print(message.content)

##########################################################
# chain = LLMChain(
#     llm=chat,
#     prompt=prompt
# )

# print("\n--------------------")
# for message in chain.stream(input={"content": "tell me a joke"}):
#     print(message)

# Create a new class for override the stream method
class StreamingChain(LLMChain):
    def stream(self, input):
        # print("\nself(input)")
        # print(self(input))
        # print('hi there!')
        #- - -
        #Generator to produces string:
        # yield 'hi'
        # yield 'there'

        def task():
            self(input) #Run the chain
        Thread(target=task).start()
        
        while True:
            token = queue.get()
            if token is None:
                break
            yield token


chain = StreamingChain(llm=chat, prompt=prompt)
# chain.stream('xampp')
# print(chain('tell me a joke'))
for out in chain.stream(input={"content":"tell me a joke"}):
    # print("\nout")
    print(out)
    