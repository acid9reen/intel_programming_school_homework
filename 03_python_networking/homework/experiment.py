import os
from collections import namedtuple
from typing import Dict

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
    return 0


if __name__ == "__main__":
    SystemExit(main())
