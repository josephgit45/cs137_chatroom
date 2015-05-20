from network import Listener, Handler, poll
import asyncore

 
handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        print 'open'
        self.do_send('open')
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        print msg
 
 
port = 8888
server = Listener(port, MyHandler)

while 1:
    #poll(timeout=0.05) # in seconds
    #server.handler_class.found_terminator()
    server.handle_accept()
    asyncore.loop()
    server.handler_class.found_terminator()
    asyncore.loop()
    mytxt = sys.stdin.readline().rstrip()
    server.handler_class.do_send({'txt': mytxt})
    asyncore.loop()
