# Task
Measure performance for each type of server in two scenarios:\
simple request-response (echo server) and CPU bound operation
(find fibonacci number, etc)

|| Request-response | CPU bound |
| :--- |:---:|:---:|
| Socket server | 23255.81 | 0.5013 |
| Selector server | 21276.59 | 0.5042 |
| Selectors server | 13698.63 | 0.5054 |
| Flask server | 363.24 | 0.5001 |
