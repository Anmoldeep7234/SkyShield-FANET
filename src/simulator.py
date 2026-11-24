## Creating UAV Simulation

import random
from datetime import datetime

class UAVNode:
    def __init__(self, node_id):
        self.node_id = node_id

nodes = [UAVNode(f"UAV_{i}") for i in range(1, 11)]

def generate_packet():

    source = random.choice(nodes).node_id
    destination = random.choice(nodes).node_id

    while source == destination:
        destination = random.choice(nodes).node_id

    hop_count = random.randint(1,5)

    packet = {
        "timestamp": datetime.now(),
        "source": source,
        "destination": destination,
        "hop_count": hop_count,
        "packet_size": random.randint(100,1500),
        "delay": round(random.uniform(1,20),2)
    }

    return packet