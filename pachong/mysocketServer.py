# import socket
# import threading
# host = socket.gethostname()
# port = 9999
#
# s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# s.listen(5)
# print("---------Begin Listening!!---------")
# def  runThread(conn):
#     data = conn.recv(1024)
#     print("             Msg :" + data.decode("utf-8"))
#     print("-"*35)
#     conn.sendall(data)
#     conn.close()
# while True:
#     conn, addr =  s.accept()
#     print(str(addr[0])+" Connected at Port:"+str(addr[1]))
#     t = threading.Thread(target=runThread,args=(conn,))
#     t.start()
import socket
import  threading
s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host =  socket.gethostname()
port = 9999
s.bind((host,port))
s.listen(5)
print("---------Begin Listening!!---------")
def runThread(conn):
    data = conn.recv(2048)
    print("       Msg :"+data.decode("utf-8"))
    print("-"*25)
    conn.sendall(data)
    conn.close()

while True:
    conn, addr = s.accept()
    print(str(addr[0])+" connect at port :" + str(addr[1]))
    t =  threading.Thread(target=runThread, args=(conn,))
    t.start()