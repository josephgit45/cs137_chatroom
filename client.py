from network import Handler, poll, Listener
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        print msg
        
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})


def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll, name = "client_thread")
thread.daemon = True  # die when the main thread dies 
thread.start()
#thread.run()

while 1:   
    try:
        client.found_terminator()
    except:
        pass
    to_send = raw_input("send back: ")
    client.do_send("User: " + to_send + "\n")

