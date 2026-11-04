## Creating UAV Simulation

import random
from datetime import datetime

class UAVNode:
    def __init__(self, node_id):
        self.node_id = node_id

# Create 10 UAVs
nodes = [UAVNode(f"UAV_{i}") for i in range(1, 11)]

def generate_packet():
    source = random.choice(nodes).node_id
    destination = random.choice(nodes).node_id

    while destination == source:
        destination = random.choice(nodes).node_id

    packet = {
        "timestamp": datetime.now(),
        "source": source,
        "destination": destination
    }

    return packet