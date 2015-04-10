import socket, sys, time
from datetime import datetime
from thread import *

IP = ""
PORT = 54321

total_data = 0.0
start = 0
end = 0


def threadWork(client):
    start = datetime.now()
    while True:
          msg = client.recv(1024)
          if not msg:
                 pass
          else:
                 print "Client send: " + msg
                 client.send("You say: " + msg + "\r\n")
    client.close()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
except socket.error, msg:
    sys.stderr.write("[Errror] %s\n" % msg[1])
    sys.exit(1)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))
sock.listen(5)

while True:
    (csock, adr) = sock.accept()
    print "Clinet Info: ", csock, adr
    start_new_thread(threadWork, (csock,))
sock.close()










