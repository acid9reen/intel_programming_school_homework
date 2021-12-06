# Task
Measure performance for each type of server in two scenarios:\
simple request-response (echo server) and CPU bound operation
(find fibonacci number, etc)

|| Request-response | CPU bound |
| :--- |:---:|:---:|
| Socket server | 0.043 | 1994.731 |
| Selector server | 0.047 | 1982.96 |
| Selectors server | 0.073 | 1978.619 |
| Flask server | 2.753 | 1999.353 |
