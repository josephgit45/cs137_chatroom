from network import Listener, Handler, poll
import asyncore
 
handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        print msg

class MyListener(Listener):

    def on_accept(self, h):
        #add queue later
        print 'user connected'
        h.do_send('agent has been connected\n')
        self.chat(h)
    
    def chat(self,h):
        while 1:
            poll(timeout=0.05)
            to_send = raw_input("send back: ")
            if(to_send is not ""):
                h.do_send("Agent: " + to_send + "\n")

port = 8888
server = MyListener(port, MyHandler)

while 1:
    #poll(timeout=0.05) # in seconds
    server.handle_accept()

