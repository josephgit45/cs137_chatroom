from network import Handler, poll, Listener
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')
options = raw_input('What do you need help with? 1) Question, 2) Complaint, 3) Return \n')
if options == "1":
    topic = raw_input('What is your question? ')
elif options == "2":
    topic = raw_input('What is the complaint? ')
else:
    topic = raw_input('What would you like to return? ')

print "Connecting you to an agent."

class Client(Handler):
    
    def on_close(self):
        print "Goodbye."
    
    def on_msg(self, msg):
        if 'join' in msg:
            self.log += "Agent " + msg['join'] + " has joined.\n"
            print "Agent " + msg['join'] + " has joined."
            client.do_send({'join': myname, 'option': options, 'topic': topic})
        elif 'txt' in msg:
            self.log += "Agent " + msg['speak'] + " said: " + msg['txt'] + "\n"
            print "Agent " + msg['speak'] + " said: " + msg['txt']
        else:
            print "Agent is busy. Please wait."
        
host, port = 'localhost', 8888
client = Client(host, port)
    #while not client.connected:  # poll until connected
#    sleep(0.05)
client.do_send({'join': myname, 'option': options, 'topic': topic})

def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds
                            
thread = Thread(target=periodic_poll, name = "client_thread")
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    to_send = sys.stdin.readline().rstrip()
    client.log += "Client said: " + to_send + "\n"
    if(to_send==":q"):
        client.do_send({'speak': myname, 'quit': to_send})
        client.do_close()
    elif(to_send==":s"):
        print "Saving to log.txt file"
        logFile = open("log.txt", "w+")
        logFile.write("CHAT LOG:\n")
        logFile.write(client.log)
        logFile.close()
    elif(to_send==":e"):
        print"      ___ "
        print"   .-*)) `*-."
        print"  /*  ((*   *'."
        print" |   *))  *   *\ "
        print" | *  ((*   *  /"
        print"  \  *))  *  .'"
        print"   '-.((*_.-'"

        client.log +="      ___ \n"
        client.log +="   .-*)) `*-.\n"
        client.log +="  /*  ((*   *'.\n"
        client.log +=" |   *))  *   *\ \n"
        client.log +=" | *  ((*   *  /\n"
        client.log +="  \  *))  *  .'\n"
        client.log +="   '-.((*_.-'\n"
    else:
        client.do_send({'speak': myname, 'txt': to_send})

