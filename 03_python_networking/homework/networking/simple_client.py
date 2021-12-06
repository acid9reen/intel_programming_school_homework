import socket

from utils import timeit

SERVER_HOST = "localhost"
SERVER_PORT = 8090


@timeit
def run_client(num_requests: int = 500) -> None:

    client_socket = socket.socket()
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    for __ in range(num_requests):

        print("Sending ping")

        client_socket.send("Ping".encode())

        print("Receiving response...")
        response = client_socket.recv(4096)
        print(f"Response: {response} was received")

    print("Closing connection")
    client_socket.close()


if __name__ == "__main__":
    print(run_client(100))
