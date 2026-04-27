import socket

client = socket.socket()

client.connect(("127.0.0.1", 9999))

while True:
    msg = input("Enter message: ")
    client.send(msg.encode())