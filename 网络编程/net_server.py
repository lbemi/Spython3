import socket
import sys
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server.bind((host,port))
server.listen(5)
while True:
    clientsocket, addr = server.accept()
    print('连接地址：%s' % str(addr))
    msg = '欢迎访问菜鸟教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()