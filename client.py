from network import Handler, poll, Listener
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')
options = raw_input('What do you need help with? 1) Question, 2) Complaint, 3) Return \n')

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        print msg
        
host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname, 'option': options})
while not client.connected:  # poll until connected
    poll(timeout=0.1)

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll, name = "client_thread")
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    to_send = sys.stdin.readline().rstrip()
    client.do_send({'speak': myname, 'txt': to_send})

