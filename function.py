import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error as msg:
    print(msg)
    sys.exit()

print('Socket Create')
try:
    host = 'www.zhihu.com'
    port = 80
    remote_ip = socket.gethostbyname(host)
    print(host,remote_ip)
except socket.gaierror:
    print('sss')
s.connect([remote_ip, port])



message =  "GET / HTTP/1.1\r\n\r\n"
message = message.encode('utf-8')
try:
    s.sendall(message)
except socket.error as msg :
    print(msg)
    sys.exit()
print('Message send successfully')

reply = s.recv(4096)
print(reply)
s.close()