import socket, sys

IP = "***.***.***.***"
PORT = 54321

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    sys.stderr.write("[Error] %s\n" % msg[1])
    sys.exit(1)

try:
    sock.connect((IP,PORT))
except socket.error, msg:
    sys.stderr.write("[Error] %s\n" % msg[1])
    exit(1)
count = 0
direct = 0
while True:
    if count <= 0:
       direct = 1
    if count >= 10000:
       direct = -1
    if direct == 1:
       count = count + 1
    if direct ==-1:
       count = count - 1
    sock.send("Hello~ :D "+ repr(count) +"\r\n")
    print sock.recv(1024)

sock.close()




