import socket

tcp_socket = socket.create_connection(('localhost', 8081))

try:
    data = str.encode('TCP client')
    tcp_socket.sendall(data)
finally:
    print('Closing TCP socket')
    tcp_socket.close()