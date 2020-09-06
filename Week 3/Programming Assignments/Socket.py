import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

data = my_socket.recv(512)
while len(data) >= 1:
    print(data.decode())
    data = my_socket.recv(512)

my_socket.close()