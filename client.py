import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 7538
connection.connect(("127.0.0.2", PORT))

rd = connection.recv(1024)
print(rd.decode('utf8'))

rd = connection.recv(1024)
print(rd.decode('utf8'))

connection.send("nice to meet U ,server".encode())
#changes
connection.close()
