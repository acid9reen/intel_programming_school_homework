import requests

from utils import ExperimentStage, timeit


@timeit
def run_requests_client(stage: ExperimentStage, num_requests: int = 500) -> None:
    url = (
        "http://127.0.0.1:8090/"
        if stage == ExperimentStage.REQUEST_RESPONSE
        else "http://127.0.0.1:8090/fib"
    )

    for __ in range(num_requests):
        request = requests.get(url)


if __name__ == "__main__":
    print(run_requests_client(ExperimentStage.REQUEST_RESPONSE, 100))
