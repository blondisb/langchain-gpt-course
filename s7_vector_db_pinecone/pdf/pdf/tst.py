from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv

load_dotenv()

class StreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token, **kwars):
        print(token)

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

class StreamingChain(LLMChain):
    def stream(self, input):
        print(self(input))
        # print('hi there!')
        yield 'hi'
        yield 'there'

chain = StreamingChain(llm=chat, prompt=prompt)
# chain.stream('xampp')
# print(chain('tell me a joke'))
for out in chain.stream('zzzz'):
    print(out)
    