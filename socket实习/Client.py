import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8081))

print(s.recv(1024).decode('utf-8'))
while True:
    date = input(':')
    s.send(date.encode('utf-8'))#发送
    exit_exit = s.recv(1024).decode('utf-8')#接收
    if exit_exit == '退出':
        print(exit_exit)
        sys.exit()
    
    else:
        print(exit_exit)





