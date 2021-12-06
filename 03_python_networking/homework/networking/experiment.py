import multiprocessing
import os
from collections import namedtuple
from timeit import default_timer as timer
from typing import Dict

import flask_server
import requests_client
import selector_server
import selectors_server
import simple_client
import socket_server
from utils import ExperimentStage

Record = namedtuple("Record", ["request_response", "cpu_bound"])
ExperimentResult = Dict[str, Record]


def get_script_folder_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def gen_table(experiment_result: ExperimentResult) -> str:
    table = ""
    for experiment_name, record in experiment_result.items():
        table += (
            f"| {experiment_name} | {record.request_response} | {record.cpu_bound} |\n"
        )

    return table


def gen_readme(experiment_result: ExperimentResult) -> None:
    task_descr = (
        "# Task\n"
        "Measure performance for each type of server in two scenarios:\\\n"
        "simple request-response (echo server) and CPU bound operation\n"
        "(find fibonacci number, etc)\n"
    )
    table_header = "|| Request-response | CPU bound |\n| :--- |:---:|:---:|\n"
    table_content = gen_table(experiment_result)
    readme_filepath = os.path.join(get_script_folder_path(), "README.md")

    with open(readme_filepath, "w", encoding="utf-8") as readme:
        readme.write(task_descr + "\n" + table_header + table_content)


def main() -> int:
    servers = {
        "Socket server": socket_server.run_socket_server,
        "Selector server": selector_server.run_selector_server,
        "Selectors server": selectors_server.run_selectors_server,
        "Flask server": flask_server.run_flask_server,
    }
    clients = {
        "Simple client": simple_client.run_client,
        "Requests client": requests_client.run_requests_client,
    }

    experiment_result = {
        "Socket server": Record(0, 0),
        "Selector server": Record(0, 0),
        "Selectors server": Record(0, 0),
        "HTTP server": Record(0, 0),
    }

    requests = 2
    os.system("sudo kill -9 $(sudo lsof -t -i:8090)")

    for server_name, run_server in servers.items():
        times = []

        for stage in ExperimentStage:
            server_args = (stage,) if server_name == "Flask server" else tuple([])
            server_process = multiprocessing.Process(
                target=run_server, args=server_args
            )
            server_process.start()

            client, client_args = (
                (clients["Requests client"], (stage, requests))
                if server_name == "Flask server"
                else (clients["Simple client"], (requests,))
            )

            client_process = multiprocessing.Process(target=client, args=client_args)

            start = timer()
            client_process.start()
            client_process.join()
            end = timer()

            times.append(f"{requests / (end - start):.4f}")

            server_process.terminate()
            os.system("sudo kill -9 `sudo lsof -t -i:8090`")

        experiment_result[server_name] = Record(*times)

    gen_readme(experiment_result)

    return 0


if __name__ == "__main__":
    SystemExit(main())
