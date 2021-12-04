import socket

SERVER_HOST = "localhost"
SERVER_PORT = 8090

client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))

print("Sending ping")
client_socket.send("Ping".encode())

print("Receiving response...")
response = client_socket.recv(4096)
print(f"Response: {response} was received")

print("Closing connection")
client_socket.close()
