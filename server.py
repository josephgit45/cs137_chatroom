from network import Listener, Handler, poll
import asyncore
 
handlers = {}  # map client handler to user name
#clients = set()
clients = []

class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        if self in clients[0:2]:
            for c in clients[0:2]:
                if c is not self:
                    c.do_send(msg)
                elif 'quit' in msg.keys() and c is self:
                    print msg['speak'] + " user left."
                    clients.remove(c)
                    break

class MyListener(Listener):

    def on_accept(self, h):
        #if len(clients) >= 2:
        #    while len(clients) >= 2:
        #        poll(timeout=0.1)
        print 'user connected'
        clients.append(h)

port = 8888
server = MyListener(port, MyHandler)

while 1:
    poll(timeout=0.05) # in seconds
#server.handle_accept()

