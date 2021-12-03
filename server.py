import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = socket.gethostbyname(socket.gethostname())
PORT = 7538
listener.bind(("127.0.0.2", PORT))
listener.listen(1)
connection, address = listener.accept()

connection.send("Hello, Client, connect ".encode('utf8'))
connection.send("again ,hello".encode('utf8'))

while True:
    data_output = ''
    while True:
        data = connection.recv(1024).decode("utf8")
        data_output += data
        if not data:
            break
    if data_output != "":
        print(data_output)

