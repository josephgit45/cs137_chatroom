from server import MyHandler
from client import Client

server = Listerner(8888, MyHandler)
client = Client('localhost', 8888)

poll(timeout=2)
client.do_send('Anni')
server.collect_incoming_data()


