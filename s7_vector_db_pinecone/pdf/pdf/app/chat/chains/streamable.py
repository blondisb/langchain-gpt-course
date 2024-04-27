from app.chat.callbacks.stream import StreamingHandler
from threading import Thread
from queue import Queue

# Create a new class for override the stream method # class StreamingChain(LLMChain):
class StreamableChain:    
    def stream(self, input):
        # print("\nself(input)") # print(self(input)) # print('hi there!') #- - - #Generator to produces string: # yield 'hi'# yield 'there'

        # Each user need and independent queue and handler
        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            #Run the chain # callbacks: create a separe queue and separe handler in every call
            self(input, callbacks=[handler])
        Thread(target=task).start()
        
        while True:
            token = queue.get()
            if token is None:
                break
            yield token