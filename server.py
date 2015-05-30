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
                    if len(clients) > 2:
                        clients[2].do_send({'join': ""})
                    clients.remove(c)
        else:
            self.do_send({'busy': "Please wait."})

class MyListener(Listener):

    def on_accept(self, h):
        print 'user connected'
        clients.append(h)

port = 8888
server = MyListener(port, MyHandler)
print "server is running..."

while 1:
    poll(timeout=0.05) # in seconds
#server.handle_accept()

