# Task
Measure performance for each type of server in two scenarios:\
simple request-response (echo server) and CPU bound operation
(find fibonacci number, etc)

|| Request-response | CPU bound |
| :--- |:---:|:---:|
| Socket server | 421.3946 | 402.4947 |
| Selector server | 427.3785 | 435.6794 |
| Selectors server | 436.7836 | 429.9306 |
| HTTP server | 0 | 0 |
| Flask server | 219.0018 | 198.8325 |
