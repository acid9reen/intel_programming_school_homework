import socket

from utils import ExperimentStage, fib


def get_server_socket():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 8090))
    server_sock.listen()

    return server_sock


def run_socket_server(stage: ExperimentStage):
    server_socket = get_server_socket()

    while True:
        print("Waiting new connection...")
        client_socket, client_addr = server_socket.accept()
        print(f"Connection has been received from {client_addr[0]}:{client_addr[1]}")
        counter = 0

        while True:
            counter += 1
            request = client_socket.recv(4096)
            print(f"Received: {request}")

            if request:
                print("Sending message to client...")

                if stage == ExperimentStage.CPU_BOUND:
                    __ = fib()

                client_socket.send("Pong".encode())
            else:
                print("Client has gone. Closing client socket...")
                client_socket.close()
                break


if __name__ == "__main__":
    run_socket_server(ExperimentStage.CPU_BOUND)
