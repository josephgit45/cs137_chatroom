from network import Handler, poll, Listener
import sys
from threading import Thread
from time import sleep


myname = raw_input('Agent, what is your name? ')

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        if 'join' in msg:
            print "User " + msg['join'] + " has joined."
        elif 'txt' in msg:
            print "User " + msg['speak'] + " said: " + msg['txt']
        elif 'quit' in msg:
            print "User " + msg['speak'] + " has left."

host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})
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

