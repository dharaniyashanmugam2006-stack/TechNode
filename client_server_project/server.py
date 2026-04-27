import socket

server = socket.socket()
server.bind(("0.0.0.0", 9999))
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024).decode()
    print("Client:", data)