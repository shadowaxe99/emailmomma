```python
import random
from typing import List

class Server:
    def __init__(self, id: int):
        self.id = id
        self.load = 0

    def add_load(self, load: int):
        self.load += load

    def remove_load(self, load: int):
        self.load -= load

class LoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers

    def distribute_load(self, load: int):
        # Sort servers by load
        self.servers.sort(key=lambda server: server.load)

        # Distribute load to the server with the least load
        self.servers[0].add_load(load)

    def remove_load(self, server_id: int, load: int):
        for server in self.servers:
            if server.id == server_id:
                server.remove_load(load)
                break

    def get_server_status(self):
        status = {}
        for server in self.servers:
            status[server.id] = server.load
        return status

# Initialize servers
servers = [Server(i) for i in range(10)]

# Initialize load balancer
load_balancer = LoadBalancer(servers)

# Simulate incoming network traffic
for _ in range(1000):
    load = random.randint(1, 10)
    load_balancer.distribute_load(load)

# Print server status
print(load_balancer.get_server_status())
```