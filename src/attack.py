import random

GRAYHOLE_NODE = "UAV_5"
ROUTE_POISON_NODE = "UAV_7"

def apply_attack(packet):

    # Default values
    packet["status"] = "Forwarded"
    packet["route_status"] = "Normal"

    # Grayhole Attack
    if packet["source"] == GRAYHOLE_NODE:

        if random.random() < 0.55:
            packet["status"] = "Dropped"

    # Route Poisoning Attack
    if packet["source"] == ROUTE_POISON_NODE:

        if random.random() < 0.40:
            packet["route_status"] = "Poisoned"

    return packet