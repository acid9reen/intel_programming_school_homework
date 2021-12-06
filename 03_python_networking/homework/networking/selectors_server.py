import selectors
import socket

from utils import ExperimentStage, fib

selector = selectors.DefaultSelector()


def server() -> None:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 8090))
    server_sock.listen()

    selector.register(
        fileobj=server_sock, events=selectors.EVENT_READ, data=accept_connection
    )


to_monitor = []


def accept_connection(server_sock: socket.socket, stage: ExperimentStage) -> None:
    client_socket, client_addr = server_sock.accept()
    print(f"Connection has been received from {client_addr[0]}:{client_addr[1]}")
    selector.register(
        fileobj=client_socket, events=selectors.EVENT_READ, data=send_message
    )


def send_message(client_sock: socket.socket, stage: ExperimentStage) -> None:
    request = client_sock.recv(4096)
    print(f"Received: {request.decode()}")

    if request:
        print("Sending Ping to client...")

        if stage == ExperimentStage.CPU_BOUND:
            __ = fib()

        client_sock.send("Pong".encode())
    else:
        print("Client has gone. Closing client socket...")
        selector.unregister(client_sock)
        client_sock.close()


def event_loop(stage: ExperimentStage):
    while True:
        events = selector.select()
        for key, __ in events:
            callback_function = key.data
            callback_function(key.fileobj, stage)


def run_selectors_server(stage: ExperimentStage):
    server()
    event_loop(stage)


if __name__ == "__main__":
    run_selectors_server(ExperimentStage.CPU_BOUND)
