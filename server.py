from network import Listener, Handler, poll
import asyncore
 
handlers = {}  # map client handler to user name
clients = set()
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        for c in clients:
            if c is not self:
                c.do_send(msg)

class MyListener(Listener):

    def on_accept(self, h):
        print 'user connected'
        clients.add(h)
        h.do_send('agent has been connected\n')

port = 8888
server = MyListener(port, MyHandler)

while 1:
    poll(timeout=0.05) # in seconds
#server.handle_accept()

